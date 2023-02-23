from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vaderSentiment
import uvicorn
import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from spotipy import MemoryCacheHandler, CacheFileHandler


load_dotenv()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Recs_Model(BaseModel):  #Request body model for /recommendations
    type: str
    term: str
    songs: int
    sentence: str

class sentiment_model(BaseModel):
    sentence: str
                        ### Functions ###

def sentiment(sentence):
    analyzer = SentimentIntensityAnalyzer() #Instance of VADER's polarity analyzer
    target: str = sentence #The sentence being tested.
    sentiment_scores = analyzer.polarity_scores(target)
    sentiment_scores['compound'] = (sentiment_scores['compound'] + 1) / 2 #Normailizing negative values to fit between 0 and 1
    return sentiment_scores
                        
def recommendations(type,term: str,num_songs: int, sentence: str):
    #Create playlist based on either the users' top 5 artists or tracks. The "valence" is my target value, 
    #determining the mood of the playlist. The valence will be determined by sentiment analysis.
    sentiment_score = sentiment(sentence)
    if type == "artists":
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_dict = {} #Holds all data need for the frontend as well as artist URI for song recommendations
        for artist in top_artists['items']:
            artist_dict[artist['name']] = [artist['images'][0]['url'], artist['uri']] #{"artist name" : ["artist image url", "artist uri"]}
        artist_seeds = [] #Seed used to base your playlist off of
        for items in artist_dict.values():
            artist_seeds.append(items[1])
        
        song_recs = spot.recommendations(seed_artists= artist_seeds,limit= num_songs, target_valence=sentiment_score['compound'])
        tracks = {}
        track_num = 0
        for track in song_recs['tracks']:
            tracks[track_num] = track['uri']
            track_num += 1
        current_user = spot.me()['id']
        playlist = spot.user_playlist_create(
            user = current_user ,
            name = "Sentify Playlist",
            description = f"Your sentiment score was: {sentiment_score}" )

        spot.playlist_add_items(
            playlist_id= playlist['id'], 
            items = list(tracks.values())
            ) 

        spot.playlist_change_details(playlist_id = playlist['id'], public = False )
        print(playlist['id'])
        # print(song_recs)
        # print(artist_dict)
        # print(tracks)
    elif type == "tracks":
        top_tracks = spot.current_user_top_tracks(limit=5,time_range=term)
        track_dict = {}

        for track in top_tracks['items']:
            track_dict[track['name']] = track['uri'] #{"track name" : "track uri"}
        track_seeds = [] #Seed used to base your playlist off of
        for item in track_dict.values():
            track_seeds.append(item)

        song_recs = spot.recommendations(seed_tracks= track_seeds, limit= num_songs, target_valence=sentiment_score['compound'])
        tracks = {}
        track_num = 0
        for track in song_recs['tracks']:
            tracks[track_num] = track['uri']
            track_num += 1
        current_user = spot.me()['id']
        playlist = spot.user_playlist_create(
            user = current_user ,
            name = "Sentify Playlist",
            public = False,
            description = f"Your sentiment score was: {sentiment_score}" )

        spot.playlist_add_items(
            playlist_id= playlist['id'], 
            items = list(tracks.values())
            ) 

        print(playlist['id'])

def login():
    spot_client = os.environ["spotify_client_id"]
    spot_token = os.environ["spotify_token"]
    redirect = os.environ["redirect_uri"]
    scopes = "user-top-read,playlist-read-private,user-top-read, playlist-modify-public"
        
    
    auth_manager = SpotifyOAuth(
        client_id= spot_client,
        client_secret=spot_token,
        redirect_uri= redirect,
        scope=scopes,
        cache_handler=MemoryCacheHandler(token_info=None)
    )
    
    global spot
    spot = spotipy.Spotify(auth_manager=auth_manager)
    user = spot.me()['id']
    user_json = {'current_user': user}
    return user_json




def tops(choice,term):
    if choice == 'artists':
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_json = []
        for artist in top_artists['items']:
            artist_dict = {}
            artist_dict['Name'] = artist['name']
            artist_dict['Photo'] = artist['images'][0]['url']
            artist_dict['Genres'] = artist['genres']
            artist_dict['Popularity'] = artist['popularity']
            artist_json.append(artist_dict)
            

        return artist_json

        # print(top_artists)
    elif choice == 'tracks':
        top_tracks = spot.current_user_top_tracks(limit=5, time_range=term)
        track_json = []
        for tracks in top_tracks['items']:
            track_dict = {}
            track_dict['Name'] = tracks['name']
            artists_list = [] #There can be more than one artist on a track
            for artist in tracks['artists']:
                artists_list.append(artist['name'])
            track_dict['Artists'] = artists_list
            track_dict['Cover'] = tracks['album']['images'][0]
            track_dict['Popularity'] = tracks['popularity']
            track_json.append(track_dict)

        return track_json


                            ### ENDPOINTS ###

@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

@app.get("/login", response_class=JSONResponse)
def spotify_login():
    result = login()
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)
@app.post("/recommendations", response_class=PlainTextResponse)
def recs(body: Recs_Model):
    recommendations(body.type, body.term, body.songs, body.sentence)
    return f"{body.songs} added to your new playlist"

@app.post("/sentiment", response_class=JSONResponse)
def sentiment_test(body: sentiment_model):
    result = sentiment(body.sentence)
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)

@app.get("/tops/{seed_type}/{seed_range}", response_class=JSONResponse)
def get_tops(seed_type,seed_range):
    result = tops(seed_type, seed_range)
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))