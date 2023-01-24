import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv #pip install python-dotenv 
import datetime
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vaderSentiment
load_dotenv()

__all__ = ["login", "recommendations"]

"""This file was originally to be used on in main.py, but I had issues with variables. So, this will be a scratch pad. 
However the function used here can be found in the FUNCTION section in main.py  """

def login():
    spot_client = os.environ["spotify_client_id"]
    spot_token = os.environ["spotify_token"]
    redirect = os.environ["redirect_uri"]
    scopes = [
        "user-top-read",
        "playlist-read-private",
        "user-top-read"
    ]
    auth_manager = SpotifyOAuth(
        client_id= spot_client,
        client_secret=spot_token,
        redirect_uri= redirect,
        scope=scopes
    )
    
    global spot
    spot = spotipy.Spotify(auth_manager=auth_manager)
    user = spot.me()['id']

    return print("Current user: {}".format(user)), spot

def recommendations(type,term: str,num_songs: int, valence: int = None):
    #Create playlist based on either the users' top 5 artists or tracks. The "valence" is my target value, 
    #determining the mood of the playlist. The valence will be determined by sentiment analysis.
    if type == "artist":
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_dict = {} #Holds all data need for the frontend as well as artist URI for song recommendations
        for artist in top_artists['items']:
            artist_dict[artist['name']] = [artist['images'][0]['url'], artist['uri']] #{"artist name" : ["artist image url", "artist uri"]}
        artist_seeds = [] #Seed used to base your playlist off of
        for items in artist_dict.values():
            artist_seeds.append(items[1])
        
        song_recs = spot.recommendations(seed_artists= artist_seeds,limit= num_songs)
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
            description = "Creating playist based on how you feel 😉" )

        spot.playlist_add_items(
            playlist_id= playlist['id'], 
            items = list(tracks.values())
            ) 

        spot.playlist_change_details(playlist_id = playlist['id'], public = False )
        print(playlist['id'])
        # print(song_recs)
        # print(artist_dict)
        # print(tracks)
    elif type == "track":
        top_tracks = spot.current_user_top_tracks(limit=5,time_range=term)
        track_dict = {}

        for track in top_tracks['items']:
            track_dict[track['name']] = track['uri'] #{"track name" : "track uri"}
        track_seeds = [] #Seed used to base your playlist off of
        for item in track_dict.values():
            track_seeds.append(item)

        song_recs = spot.recommendations(seed_tracks= track_seeds, limit= num_songs)
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
            description = "Creating playist based on how you feel 😉" )

        spot.playlist_add_items(
            playlist_id= playlist['id'], 
            items = list(tracks.values())
            ) 

        print(playlist['id'])

def sentiment(sentence):
    analyzer = SentimentIntensityAnalyzer() #Instance of VADER's polarity analyzer
    target: str = sentence #The sentence being tested.
    sentiment_scores = analyzer.polarity_scores(target)
    if sentiment_scores['compound'] > 0 and (sentiment_scores['pos'] != 0 or sentiment_scores['neg'] != 0):
        sentiment_valence = {'valence' : sentiment_scores['compound']}
        sentiment_scores.update(sentiment_valence)
        print(sentiment_scores)
        print('0')
    elif sentiment_scores['compound'] < 0:
        sentiment_valence = {'valence' : sentiment_scores['pos']}
        sentiment_scores.update(sentiment_valence)
        print(sentiment_scores)
        print('1')
    elif sentiment_scores['pos'] == 0 and (sentiment_scores['neg'] == 0 and sentiment_scores['neu'] != 0):
        sentiment_valence = {'valence' : sentiment_scores['neu']}
        sentiment_scores.update(sentiment_valence)
        print(sentiment_scores)
        print('2')

def tops(choice,term):
    if choice == 'artists':
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_json = [] # Allows to add multiple dict, for json respone in api
        for artist in top_artists['items']:
            artist_dict = {}
            artist_dict['Name'] = artist['name']
            artist_dict['Photo'] = artist['images'][0]['url']
            artist_dict['Genres'] = artist['genres']
            artist_dict['Popularity'] = artist['popularity']
            artist_json.append(artist_dict)
            # print(artist_dict['Name'])

        print(artist_json)

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
        print(track_json)


if __name__ == "__main__":
    login()
    tops('tracks','short_term')
