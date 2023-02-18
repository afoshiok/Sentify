import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv #pip install python-dotenv 

#My goal here is to create a Spotipy cache handler for FastAPI
class CacheHandler():
    """
    An abstraction layer for handling the caching and retrieval of
    authorization tokens.
    Custom extensions of this class must implement get_cached_token
    and save_token_to_cache methods with the same input and output
    structure as the CacheHandler class.
    """

    def get_cached_token(self):
        """
        Get and return a token_info dictionary object.
        """
        # return token_info
        raise NotImplementedError()

    def save_token_to_cache(self, token_info):
        """
        Save a token_info dictionary object to the cache and return None.
        """
        raise NotImplementedError()
        return None


class FastApiSessionCacheHandler(CacheHandler):
    def __init__(self) -> None:
        def __init__(self, session):
            self.session = session