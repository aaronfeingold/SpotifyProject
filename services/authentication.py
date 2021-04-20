import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAuthenticator:
  def __init__(self, client_id, client_secret):
    self.client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials)

  