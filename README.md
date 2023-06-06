# Sentify

## At-A-Glance

**Problem:** As an avid music lover, I'm constantly looking for new music to add to my various playlists. Although Spotify has by far the best recommendation system when compared to other music streaming platforms (in my opinion), there few options to get on-demand new music recommendations. The main way, outside of album releases, I find music is through either Spotify's "Discover Weekly" or "Daily Mix" playlists.

**Solution:** A web application that generates a Spotify playlist of up to 100 songs based on your top artists/tracks of a given time period. I added the sentiment analysis feature, because at the time I had the idea for this project I recently completed an intership which focus heavily on sentiment analysis and wanted to play around with its use.

## Tech Stack

**Backend:**
- **Language(s):**
    <p align="left">
      <a href="https://skillicons.dev">
        <img src="https://skillicons.dev/icons?i=py" />
      </a>
    </p>


- **Libraries/Frameworks:** Vader Sentiment Analysis, FastAPI (Also tried using Flask for REST API creation)

**Frontend:**
- **Language(s):**
    <p align="left">
      <a href="https://skillicons.dev">
        <img src="https://skillicons.dev/icons?i=ts,js,html,css" />
      </a>
    </p>


- **Libraries/Frameworks:** Vue, Tailwind, Daisy UI, Axios

## Running the application

Before you do anything the terminal, you need to set up two .env, one in the root directory of the `/api` and one in the root directory of the `/sentify` .

```.env
# .env in /api directory
spotify_client_id = "Spotify client id from Spotify Developer Poratal"
spotify_token = "Spotify token from Spotify Developer Poratal"
redirect_uri = "http://desired_redirect_uri" #You determine this in the Spotify Developer Poratal
PORT = 5000 #Or any port you want to run your API on.
```

```.env
#.env in /sentify directory
PORT = 3000 #Or any port you want to run your frontend on.
VITE_API_BASE_URL = "http://api_url"
```

Now you will install you dependencies in both the `/api` and `/sentify` directories.

For `/sentify`:
```cmd
cd sentify
npm install
```
