from decouple import config
from twilio.rest import Client

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# dev_songs = [{'track_href': 'https://open.spotify.com/track/6gfb1SpowOErvfNBkFZT45', 'track_artist': 'Ghost', 'track_name': 'Con Clavi Con Dio'}, {'track_href': 'https://open.spotify.com/track/3qNb7IfeHSWVIyAeYkZXAa', 'track_artist': 'Khamari', 'track_name': 'The Heat'}, {'track_href': 'https://open.spotify.com/track/5VKEsChbUowEF2BT0gJSGX', 'track_artist': 'Gunship', 'track_name': 'Tech Noir'}]

class SendTextMessage:
  def __init__(self, songs):
    self.songs = songs
    self.message = self.set_message()

  
  def set_message(self):
    songs = self.songs
    
    message = []

    for song in songs:
      artist = song["track_artist"]
      track = song["track_name"]
      song_link = song["track_href"]
      sentance = f'{track} by: {artist}. Link here: {song_link}'
      message.append(sentance)

    return message

  
  def send_sms(self):
    return self.message




# message = client.messages \
#             .create(
#                  body=self.message,
#                  from_='+13478307901',
#                  to='+12017879112'
#              )
# print(message.sid)
# text_sender = SendTextMessage(songs=dev_songs)

# print(text_sender.message)


