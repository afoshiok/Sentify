import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pprint
load_dotenv()

spot_client = os.environ["spotify_client_id"]
spot_token = os.environ["spotify_token"]
scopes = [] #Scopes I need to get this app to work. List of scopes here: https://developer.spotify.com/documentation/general/guides/authorization/scopes/ 
auth_manager = SpotifyOAuth(
    client_id=spot_client,
    client_secret=spot_token,
    redirect_uri="http://localhost:8080"
    )
spot = spotipy.Spotify(auth_manager=auth_manager)

def get_recs():
    recommendations = spot.recommendations(
        seed_artists=['https://open.spotify.com/artist/7gW0r5CkdEUMm42w9XpyZO?si=8N9RAXfZTW6zxvFSqfyrPw'], # To seed multiple artist create a list of their URLs, IDs or URIs (Maximum of 5 artists)
        seed_tracks= None, #I want this app to seed the users previously listened to tracks. I need a "user-read-recently-played" scope
        limit= 15 #The api can generate a maximum of a 100 songs, I haven't settled yet on how many songs I want in the playlist.
        )