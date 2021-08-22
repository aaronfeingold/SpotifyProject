import requests

class SongGetter:
  def __init__(self, token):
    self.token = token

  def get_song(self, name):
    id = self.get_playlist_id(name)
    song = self.get_playlist_items(id)

    return song

  
  def get_playlist_id(self, name):
      # make a request for for the user's playlists
      url = f"https://api.spotify.com/v1/users/{name}/playlists"
      headers = {
        "Authorization": "Bearer " + self.token
      }
      res = requests.get(url=url, headers=headers)
      # select the id of the first playlist
      playlist_id = res.json()['items'][0]['id']

      return playlist_id


  def get_playlist_items(self, id):
      url = f"https://api.spotify.com/v1/playlists/{id}/tracks"
      headers = {
        "Authorization": "Bearer " + self.token
      }

      res = requests.get(url=url, headers=headers)
      # grab the first track, its external url, artist name and track name
      track = res.json()["items"][0]["track"]
      track_href = track["external_urls"]["spotify"]
      track_artist = track["artists"][0]["name"]
      track_name = track["name"]

      song = {"track_href": track_href, "track_artist": track_artist, "track_name": track_name}

      return song
