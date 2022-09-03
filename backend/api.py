from fastapi import FastAPI
from create_playlist import create_playlist,find_playlist,get_seeds,get_recs

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}