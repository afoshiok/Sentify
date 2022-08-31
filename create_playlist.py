import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pprint
import json
load_dotenv()

spot_client = os.environ["spotify_client_id"]
spot_token = os.environ["spotify_token"]
scopes = [
    'playlist-modify-private', #Creates private playlist for user
    'user-top-read' #Will be used for seed artist and seed track parameter in recommendation fuction
    ] #Scopes I need to get this app to work. List of scopes here: https://developer.spotify.com/documentation/general/guides/authorization/scopes/ 
auth_manager = SpotifyOAuth(
    client_id=spot_client,
    client_secret=spot_token,
    redirect_uri="http://localhost:8080",
    scope=scopes
    )
spot = spotipy.Spotify(auth_manager=auth_manager)

def get_seeds():
    top_artists = spot.current_user_top_artists(limit=5,time_range='short_term') #short_term is about 4 weeks
    top_tracks = spot.current_user_top_tracks(limit=10,time_range='short_term')
    artist_seed = []
    track_seeds = []
    for artist in top_artists['items']: #Creates a list of my top 5 artists name. NOTE: This is just for testing the list is going to contain their Spotify ID.
        artist_seed.append(artist['name'])

    for tracks in top_tracks['items']:
        track_dict = {tracks['name']:tracks['id']} #Creates a dictionary of top tracks with scheme of: {"track name" : "track id"}
        track_seeds.append(track_dict)
    return artist_seed, track_seeds

def get_recs():
    recommendations = spot.recommendations(
        seed_artists=['https://open.spotify.com/artist/7gW0r5CkdEUMm42w9XpyZO?si=8N9RAXfZTW6zxvFSqfyrPw'], # To seed multiple artist create a list of their URLs, IDs or URIs (Maximum of 5 artists)
        seed_tracks= None, #I want this app to seed the users previously listened to tracks. I need a "user-read-recently-played" scope
        limit= 15 #The api can generate a maximum of a 100 songs, I haven't settled yet on how many songs I want in the playlist.
        )


if __name__ == "__main__":
    get_seeds()