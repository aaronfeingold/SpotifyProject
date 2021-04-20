from decouple import config
from twilio.rest import Client

class SendTextMessage:
  def __init__(self, songs, account_sid, auth_token):
    self.songs = songs
    self.account_sid = account_sid
    self.auth_token = auth_token
    self.client = self.create_twilio_client()
    self.message = self.set_message()

  def create_twilio_client(self):
      new_client = Client(username=self.account_sid, password=self.auth_token)

      return new_client


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
    joined_sentances = "\n\n".join(self.message)
    final_message = self.client.messages \
                .create(
                    body=joined_sentances,
                    from_='+13478307901',
                    to='+12017879112'
                )
    return final_message

