from twilio.rest import Client

class TextFormatter():

  def format_message(songs):
    message = []

    for song in songs:
      artist = song["track_artist"]
      track = song["track_name"]
      song_link = song["track_href"]
      sentence = f'{track} by: {artist}. Link here: {song_link}'
      message.append(sentence)

    formatted_message = "\n\n".join(message)

    return formatted_message


  






