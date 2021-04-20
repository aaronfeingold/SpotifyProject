from services.authentication import SpotifyAuthenticator
from services.song_getter import SongGetter
from services.texter import SendTextMessage
import json

secrets = json.loads(open("secrets.json").read())

dev_user_names = ['22gnzesxvy4aaxsab3fbxkq6y', 'a.dglazier', '1214200651']
dev_numbers = ['+12017879112']

sa = SpotifyAuthenticator(client_id=secrets["SPOTIFY_CLIENT_ID"], client_secret=secrets["SPOTIFY_CLIENT_SECRET"])
song_getter = SongGetter(sp=sa.sp)
songs = [song_getter.get_song(name) for name in dev_user_names]
text_sender = SendTextMessage(songs=songs, numbers=dev_numbers, account_sid=secrets["TWILIO_ACCT_SID"], auth_token=secrets["TWILIO_AUTH_TOKEN"])
text_sender.send_sms()
