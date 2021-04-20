from services.authentication import Authenticator
from services.song_getter import SongGetter
from services.texter import SendTextMessage
import json
secrets = json.loads(open("secrets.json").read())

user_names = ['22gnzesxvy4aaxsab3fbxkq6y', 'a.dglazier', '1214200651']

authenticator = Authenticator(client_id=secrets["CLIENT_ID"], client_secret=secrets["CLIENT_SECRET"])
song_getter = SongGetter(sp=authenticator.sp)
songs = [song_getter.get_song(name) for name in user_names]
text_sender = SendTextMessage(songs=songs)
text_sender.send_sms()

