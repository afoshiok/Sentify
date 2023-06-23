import logging
from dotenv import load_dotenv
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import uvicorn
import os
from fastapi import FastAPI, Request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from spotipy import CacheHandler, MemoryCacheHandler




load_dotenv()

logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000" #For debugging
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Recs_Model(BaseModel): 
    type: str
    term: str
    songs: int
    sentence: str

class sentiment_model(BaseModel):
    sentence: str

class SessionData(BaseModel):
    token: object


    

### Functions ###

def sentiment(sentence): 
    """
    Creates VADER Sentiment instance, analyzes the polarity of the sentence and returns
    the polarity score as well as a normalized compound score.

    """
    analyzer = SentimentIntensityAnalyzer()
    target: str = sentence 
    sentiment_scores = analyzer.polarity_scores(target)
    sentiment_scores['compound'] = (sentiment_scores['compound'] + 1) / 2

    return sentiment_scores
                        
def recommendations(type,term: str,num_songs: int, sentence: str):
    """
    Finds song recommendations with the Spotify API based on a seed type, term
    and desired number of songs. The "sentence" parameter will be passed into the 
    sentiment function and it's returned compound value will be used as the target 
    valence.

    """
    sentiment_score = sentiment(sentence)
    if type == "artists":
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_dict = {} 
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


        return [f"https://open.spotify.com/playlist/{playlist['id']}", sentiment_score]

    elif type == "tracks":
        top_tracks = spot.current_user_top_tracks(limit=5,time_range=term)
        track_dict = {}

        for track in top_tracks['items']:
            track_dict[track['name']] = track['uri'] #{"track name" : "track uri"}
        track_seeds = [] 
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
            description = f"Your sentiment score was: {sentiment_score}" )

        spot.playlist_add_items(
            playlist_id= playlist['id'], 
            items = list(tracks.values())
            )

        print(playlist['id'])
        return [f"https://open.spotify.com/playlist/{playlist['id']}", sentiment_score]

def auth(state):
    spot_client = os.environ["spotify_client_id"]
    spot_token = os.environ["spotify_token"]
    redirect = os.environ["redirect_uri"]
    scopes = "playlist-read-private,user-top-read, playlist-modify-public"
        
    
    auth_manager = SpotifyOAuth(
        client_id= spot_client,
        client_secret=spot_token,
        redirect_uri= redirect,
        scope=scopes,
        cache_handler=None
    )
    
    if state == 'login':
        global spot
        # spot = spotipy.Spotify(auth_manager=auth_manager)
        # user = spot.me()['id']
        # user_json = {'current_user': user}
        # user = spot.me()['id']
        # user_json = {'current_user': user}
        # return user_json
        auth_url = auth_manager.get_authorize_url()
        return {"auth_url": auth_url}
    
    elif state == 'callback':
        # global spot
        # auth_code = request.GET.get('code')
        # print(auth_code)
        # auth_manager.get_access_token(auth_code)
        # spot = spotipy.Spotify(auth_manager=auth_manager)
        # user = spot.current_user()['id']
        # return {'current_user': user}
        return {"message": "Please use the correct callback endpoint"}

    elif state == 'logout':
        auth_manager.cache_handler.clear()

def tops(choice,term):
    """
    Returns JSON request needed for client to preview their top artist/tracks for a 
    given term.
    
    """

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
async def healthcheck():
    return 'Health - OK'

@app.get("/auth/{state}", response_class=JSONResponse)
async def spotify_auth(state):
    result = auth(state)
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)

@app.get("/callback")
async def spotify_callback(request: Request):
    auth_code = request.query_params.get('code')
    # auth_manager = SpotifyOAuth(cache_handler=None)  # Disable caching in production
    spot_client = os.environ["spotify_client_id"]
    spot_token = os.environ["spotify_token"]
    redirect = os.environ["redirect_uri"]
    scopes = "playlist-read-private,user-top-read, playlist-modify-public"
        
    
    auth_manager = SpotifyOAuth(
        client_id= spot_client,
        client_secret=spot_token,
        redirect_uri= redirect,
        scope=scopes,
        cache_handler=None
    )
    auth_manager.get_access_token(auth_code)
    global spot
    spot = spotipy.Spotify(auth_manager=auth_manager)
    user = spot.current_user()['id']
    return {'current_user': user}

@app.post("/recommendations", response_class=JSONResponse)
async def recs(body: Recs_Model):
    result=recommendations(body.type, body.term, body.songs, body.sentence)
    repsonse = {
        'link':result[0],
        'polarity':result[1]
        }
    response_json = jsonable_encoder(repsonse)
    return JSONResponse(content=response_json)

@app.post("/sentiment", response_class=JSONResponse)
async def sentiment_test(body: sentiment_model):
    result = sentiment(body.sentence)
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)

@app.get("/tops/{seed_type}/{seed_range}", response_class=JSONResponse)
async def get_tops(seed_type,seed_range):
    result = tops(seed_type, seed_range)
    response_json = jsonable_encoder(result)
    return JSONResponse(content=response_json)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))