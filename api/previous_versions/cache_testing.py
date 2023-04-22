import os
import spotipy #pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv #pip install python-dotenv 
from fastapi_sessions.backends.implementations import InMemoryBackend #pip install fastapi_sessions
from uuid import uuid4 #pip install uuid


__all__ = [
    'MemoryCacheHandler',
    'CacheHandler'
    ]

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

class MemoryCacheHandler(CacheHandler):
    """
    A cache handler that simply stores the token info in memory as an
    instance attribute of this class. The token info will be lost when this
    instance is freed.
    """

    def __init__(self, token_info=None):
        """
        Parameters:
            * token_info: The token info to store in memory. Can be None.
        """
        self.token_info = token_info

    def get_cached_token(self):
        return self.token_info

    def save_token_to_cache(self, token_info):
        self.token_info = token_info


# session = uuid4()
# print(session)