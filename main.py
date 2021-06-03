from services.token_getter import TokenGetter
from services.song_getter import SongGetter
from services.texter import SendTextMessage
from dotenv import load_dotenv
import json
import os
import ipdb

def run_main(event):
  load_dotenv()

  sci = os.environ["SPOTIFY_CLIENT_ID"]
  scs = os.environ["SPOTIFY_CLIENT_SECRET"]
  tai = os.environ["TWILIO_ACCT_SID"]
  tat = os.environ["TWILIO_AUTH_TOKEN"]

  with open('data.json') as json_file:
    data = json.load(json_file)
  
  tg = TokenGetter(client_id=sci, client_secret=scs)
  token = tg.auth_token
  song_getter = SongGetter(token=token)
  songs = [song_getter.get_song(name) for name in data["dev_user_names"]]
  text_sender = SendTextMessage(account_sid=tai, auth_token=tat)
  message = text_sender.set_message(songs=songs)
  text_sender.send_sms(app_number=data["app_number"], numbers=data["dev_numbers"], message=message)


event = "test"
run_main(event)