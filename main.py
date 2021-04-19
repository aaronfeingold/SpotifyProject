from services.authentication import Authenticator
from services.song_getter import SongGetter
import json
secrets = json.loads(open("secrets.json").read())

authenticator = Authenticator(client_id=secrets["CLIENT_ID"], client_secret=secrets["CLIENT_SECRET"])
song_getter = SongGetter(sp=authenticator.sp)
user_names = ['22gnzesxvy4aaxsab3fbxkq6y', 'a.dglazier', '1214200651']
songs = [song_getter.get_song(name) for name in user_names]
print(songs)