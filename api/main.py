from flask import Flask
from flask import Flask, session, request, redirect
from flask_session import Session
from create_playlist import *
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import datetime
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET"])
def user_login():
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
        scope=scopes,
        )
    global spot
    spot = spotipy.Spotify(auth_manager=auth_manager)
    user = spot.me()['id']
    return f"{user}"
@app.route("/createplaylist",methods = ["POST"])
def playlist():
    login()
    new_playlist()
    find_playlist()
    get_seeds(5,0)
    get_recs()
    return "<h1>Playlist Created</h1>"

if __name__ == "__main__":
    app.run()