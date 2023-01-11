import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv #pip install python-dotenv 
import datetime
import json
load_dotenv()

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

    return print("Current user: {}".format(user))

def recommendations(type,term: str):
    if type == "artist":
        top_artists = spot.current_user_top_artists(limit=5,time_range=term)
        artist_dict = {} #Holds all data need for the frontend as well as artist URI for song recommendations
        for artist in top_artists['items']:
            artist_dict[artist['name']] = [artist['images'][0]['url'], artist['uri']]
        artist_seeds = [] #Seed used to base your playlist off of
        for items in artist_dict.values():
            artist_seeds.append(items[1])
        
        print(artist_seeds)
        # print(artist_dict)
    elif type == "track":
        top_tracks = spot.current_user_top_tracks(limit=5,time_range=term)
        return top_tracks


if __name__ == "__main__":
    login()
    recommendations("artist","medium_term")