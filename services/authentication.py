import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import CacheFileHandler

class SpotifyAuthenticator:
  def __init__(self, client_id, client_secret, cache_path):
    self.cache_handler = CacheFileHandler(cache_path=cache_path)
    self.client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret, cache_handler=self.cache_handler)
    self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials)

  