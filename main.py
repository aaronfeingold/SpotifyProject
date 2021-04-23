from services.authentication import SpotifyAuthenticator
from services.song_getter import SongGetter
from services.texter import SendTextMessage
from dotenv import load_dotenv
import json
import os

load_dotenv()

spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
spotify_client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
twilio_acct_sid = os.environ["TWILIO_ACCT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]

with open('data.json') as json_file:
  data = json.load(json_file)


def lambda_handler(event, context):
    run_main()


def run_main():
  sa = SpotifyAuthenticator(client_id=spotify_client_id, client_secret=spotify_client_secret)
  song_getter = SongGetter(sp=sa.sp)
  songs = [song_getter.get_song(name) for name in data["dev_user_names"]]
  text_sender = SendTextMessage(account_sid=twilio_acct_sid, auth_token=twilio_auth_token)
  message = text_sender.set_message(songs=songs)
  text_sender.send_sms(app_number=data["app_number"], numbers=data["dev_numbers"], message=message)



def test():
  lambda_handler(event=data["dev_cloudwatch_trigger"], context=None)


test()
