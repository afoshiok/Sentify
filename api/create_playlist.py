import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv #pip install python-dotenv 
import datetime
load_dotenv()

__all__ = ['login', 'get_seeds', 'get_recs','new_playlist', 'find_playlist']

def login():
    spot_client = os.environ["spotify_client_id"]
    spot_token = os.environ["spotify_token"]
    scopes = [
        'playlist-modify-private', #Creates private playlist for user
        'user-top-read', #Will be used for seed artist and seed track parameter in recommendation fuction
        'playlist-read-private'
        ] #Scopes I need to get this app to work. List of scopes here: https://developer.spotify.com/documentation/general/guides/authorization/scopes/ 
    auth_manager = SpotifyOAuth(
        client_id=spot_client,
        client_secret=spot_token,
        redirect_uri="http://localhost:8080",
        scope=scopes
        )
    global spot
    global user
    spot = spotipy.Spotify(auth_manager=auth_manager)
    user = spot.me()['id']

def get_seeds(artist_limit,track_limit,term='short_term'): #Sum of limits CANNOT be greater than 5
    "Gets user's top artist and track that will be used as seed for recommendation"
    global artist_seeds #Allow variables to be used withing get_recs
    global track_seeds
    
    top_artists = spot.current_user_top_artists(limit=artist_limit,time_range=term) #short_term is about 4 weeks
    top_tracks = spot.current_user_top_tracks(limit=track_limit,time_range=term)
    artist_seeds = []
    track_seeds = []
    for artist in top_artists['items']: #Creates a list of my top 5 artists ID.
        artist_id = artist['id']
        artist_seeds.append(artist_id)

    for tracks in top_tracks['items']:
        track_id = tracks['id'] #Creates a dictionary of top tracks with scheme of: {"track name" : "track id"}
        track_seeds.append(track_id)
    return print("Seeds found",term)

def get_recs(num_songs=20): #You can add up to 100 songs, but by default it adds 20 songs
    "Generates reccomendations based on user's taste in music with the help of get_seeds()"
    global new_music
    new_music = []
    recommendations = spot.recommendations(
        seed_artists=artist_seeds, # To seed multiple artist create a list of their URLs, IDs or URIs 
        seed_tracks= track_seeds, 
        limit= num_songs #The api can generate a maximum of a 100 songs, I haven't settled yet on how many songs I want in the playlist.
        )
    for song in recommendations['tracks']:
        song_uri = song['uri']
        new_music.append(song_uri)
    spot.playlist_add_items(playlist_id=sentiment_playlist[0], items=new_music, position=None)
    return print("Recommendations found")

def new_playlist():
    current_user_id = spot.me()['id'] #Gets current user id
    date = datetime.datetime.now()
    today = date.strftime('%m-%d-%Y-%H%M%S')
    new_playlist = spot.user_playlist_create(
        user=current_user_id, 
        name=f"Sentiment Playlist ({today})",
        public=False,
        collaborative=False,
        description= "Playlist generated based on your mood😉")
    return print("playlist created")

def find_playlist():
    date = datetime.datetime.now()
    today = date.strftime('%m-%d-%Y-%H%M%S')
    user_playlist = spot.current_user_playlists(limit=None, offset=0)
    global sentiment_playlist
    sentiment_playlist = []
    for playlist in user_playlist['items']:
        if playlist['name'] == f'Sentiment Playlist ({today})':
            playlist_uri = playlist['id']
            print(f"Found playlist: {playlist_uri}")
            sentiment_playlist.append(playlist_uri)
        else:
            pass
    return print("ENJOY YOUR PLAYLIST!")

if __name__ == "__main__":
    login()
    new_playlist()
    find_playlist()
    get_seeds(5,0)
    get_recs()