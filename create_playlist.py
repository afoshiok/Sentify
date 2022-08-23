"""Creating a Playlist for ML model."""
import os
from dotenv import load_dotenv
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv() #Loads enviornment variables

spotify_client = os.environ["spotify_client_id"]
spotify_token = os.environ["spotify_token"]

#Allows user to login, Spotify login opens on port 8080
SCOPE = 'playlist-read-private'
spot = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_client,
    client_secret=spotify_token,
    redirect_uri='http://localhost:8080',
    scope=SCOPE)
    )

def read_user_playlists():
    "Reads user playlists"
    res = spot.current_user_playlists(limit=None)
    for i, item in enumerate(res['items']):
        print("%d %s" % (i, item['name']))
    return res

if __name__ == "__main__":
    read_user_playlists()
