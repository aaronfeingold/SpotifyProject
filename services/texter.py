from twilio.rest import Client

class SendTextMessage:
  def __init__(self, app_number, songs, numbers, account_sid, auth_token):
    self.songs = songs
    self.numbers = numbers
    self.app_number = app_number
    self.client = Client(username=account_sid, password=auth_token)
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
    joined_sentances = "\n\n".join(self.message)
  
    for number in self.numbers:
      final_message = self.client.messages \
                  .create(
                      body=joined_sentances,
                      from_=self.app_number,
                      to=number
                  )
                

