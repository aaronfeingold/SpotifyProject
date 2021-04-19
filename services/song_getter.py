
class SongGetter:
  def __init__(self, sp):
    self.sp = sp


  def get_song(self, name):
      playlist_id = self.sp.user_playlists(name)["items"][0]["id"]
      track = self.sp.playlist_items(playlist_id)["items"][0]["track"]
      track_href = track["external_urls"]["spotify"]
      track_artist = track["artists"][0]["name"]
      track_name = track["name"]
      song = {"track_href": track_href, "track_artist": track_artist, "track_name": track_name}

      return song