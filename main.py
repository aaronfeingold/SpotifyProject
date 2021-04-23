from services.authentication import SpotifyAuthenticator
from services.song_getter import SongGetter
from services.texter import SendTextMessage
from dotenv import load_dotenv
import json
import os

def run_main(event, context):
  load_dotenv()

  sci = os.environ["SPOTIFY_CLIENT_ID"]
  scs = os.environ["SPOTIFY_CLIENT_SECRET"]
  tai = os.environ["TWILIO_ACCT_SID"]
  tat = os.environ["TWILIO_AUTH_TOKEN"]
  
  dev_user_names = ["22gnzesxvy4aaxsab3fbxkq6y", "a.dglazier", "1214200651"]
  dev_numbers = ["+12017879112"]
  app_number = ["+13478307901"]
  
  sa = SpotifyAuthenticator(client_id=sci, client_secret=scs)
  song_getter = SongGetter(sp=sa.sp)
  songs = [song_getter.get_song(name) for name in dev_user_names]
  text_sender = SendTextMessage(account_sid=tai, auth_token=tat)
  message = text_sender.set_message(songs=songs)
  text_sender.send_sms(app_number=app_number, numbers=dev_numbers, message=message)

