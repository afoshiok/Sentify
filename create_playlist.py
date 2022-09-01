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

def get_seeds(artist_limit,track_limit): #Sum of limits CANNOT be greater than 5
    "Gets user's top artist and track that will be used as seed for recommendation"
    global artist_seeds #Allow variables to be used withing get_recs
    global track_seeds

    top_artists = spot.current_user_top_artists(limit=artist_limit,time_range='short_term') #short_term is about 4 weeks
    top_tracks = spot.current_user_top_tracks(limit=track_limit,time_range='short_term')
    artist_seeds = []
    track_seeds = []
    for artist in top_artists['items']: #Creates a list of my top 5 artists ID.
        artist_id = artist['id']
        artist_seeds.append(artist_id)

    for tracks in top_tracks['items']:
        track_id = tracks['id'] #Creates a dictionary of top tracks with scheme of: {"track name" : "track id"}
        track_seeds.append(track_id)
    return print(track_seeds)

def get_recs():
    "Generates reccomendations based on user's taste in music with the help of get_seeds()"
    recommendations = spot.recommendations(
        seed_artists=artist_seeds, # To seed multiple artist create a list of their URLs, IDs or URIs 
        seed_tracks= track_seeds, 
        limit= 3 #The api can generate a maximum of a 100 songs, I haven't settled yet on how many songs I want in the playlist.
        )
    return print(json.dumps(recommendations, indent=4))

if __name__ == "__main__":
    get_seeds(2,3)
    get_recs()