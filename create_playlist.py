import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pprint
load_dotenv()

spot_client = os.environ["spotify_client_id"]
spot_token = os.environ["spotify_token"]
auth_manager = SpotifyClientCredentials(
    client_id=spot_client,
    client_secret=spot_token,
    requests_session=True
    )
spot = spotipy.Spotify(auth_manager=auth_manager)

search_inp = input("What artist are you looking for?")
result = spot.search(search_inp)
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(result)