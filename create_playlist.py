from dotenv import load_dotenv
import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv() #Loads enviornment variables

spotify_client = os.environ["spotify_client_id"]
spotify_token = os.environ["spotify_token"]

spot = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client, client_secret=spotify_token))

results = spot.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])