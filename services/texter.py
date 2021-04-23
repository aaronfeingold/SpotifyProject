from twilio.rest import Client

class SendTextMessage:
  def __init__(self, app_number, account_sid, auth_token):
    self.app_number = app_number
    self.client = Client(username=account_sid, password=auth_token)


  def set_message(self, songs):
    message = []

    for song in songs:
      artist = song["track_artist"]
      track = song["track_name"]
      song_link = song["track_href"]
      sentence = f'{track} by: {artist}. Link here: {song_link}'
      message.append(sentence)

    formatted_message = "\n\n".join(message)

    return formatted_message


  def send_sms(self, app_number, numbers, message):
    sids = []
    errors = []

    for number in numbers:
      final_message = self.client.messages \
                  .create(
                      body=message,
                      from_=app_number,
                      to=number
                  )
      if final_message.error_code:
        errors.append(final_message.error_message)
      else:
        sids.append(final_message.sid)

    if len(errors) != 0:
      return errors
    else:
      return sids


  






