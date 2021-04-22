from services.authentication import SpotifyAuthenticator
from services.song_getter import SongGetter
from services.texter import SendTextMessage
from dotenv import load_dotenv
import json
import os

class Main:

  def __init__(self):
    self.environment = self.load_environment()
    self.data = self.get_data()

  def load_environment(self):
    load_dotenv()
    self.spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
    self.spotify_client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
    self.twilio_acct_sid = os.environ["TWILIO_ACCT_SID"]
    self.twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]


  def get_data(self):
    with open('data.json') as json_file:
      data = json.load(json_file)
    return data


  def run_main(self):
    sa = SpotifyAuthenticator(client_id=self.spotify_client_id, client_secret=self.spotify_client_secret)
    song_getter = SongGetter(sp=sa.sp)
    songs = [song_getter.get_song(name) for name in self.data["dev_user_names"]]
    text_sender = SendTextMessage(songs=songs, app_number=self.data["app_number"], numbers=self.data["dev_numbers"], account_sid=self.twilio_acct_sid, auth_token=self.twilio_auth_token)
    sent_message = text_sender.send_sms()

    return sent_message


    