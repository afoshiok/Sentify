from flask import Flask, jsonify
from flask import Flask, session, request, redirect
from create_playlist import *
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import datetime
load_dotenv()

app = Flask(__name__)

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
@app.route("/playlist",methods = ["POST"])
def playlist():
    #Form user input
    seed_type = request.form['seed_type']
    songs = request.form['songs']
    seed_term = request.form['seed_term'] #Can only be "[short, medium, long]_term" or an error will be thrown

    login()
    new_playlist()
    find_playlist()
    if seed_type == 'artists':
        get_seeds(5,0,seed_term)
    elif seed_type == 'tracks':
        get_seeds(0,5,seed_term)
    get_recs(num_songs=songs)
    return jsonify(request.form)

if __name__ == "__main__":
    app.run()