from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vaderSentiment
import uvicorn
import os
from fastapi import FastAPI
from create_playlist_v2 import *

load_dotenv() 

app = FastAPI()

@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

@app.get("/login")
def spotify_login():
    login()
    return print (f"Logged as {spot.me()['id']} ")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))