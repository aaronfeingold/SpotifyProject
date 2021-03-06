from services.token_getter import TokenGetter
from services.song_getter import SongGetter
from services.text_formatter import TextFormatter
import json
import os

def run_main(event, conext):

  sci = os.environ["SPOTIFY_CLIENT_ID"]
  scs = os.environ["SPOTIFY_CLIENT_SECRET"]

  with open('data.json') as json_file:
    data = json.load(json_file)
  
  tg = TokenGetter(client_id=sci, client_secret=scs)
  token = tg.auth_token
  song_getter = SongGetter(token=token)
  songs = [song_getter.get_song(name) for name in data["dev_user_names"]]
  message = TextFormatter().format_message(songs)

  return message