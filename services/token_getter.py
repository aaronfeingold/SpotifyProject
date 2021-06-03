import requests
import base64

class TokenGetter():
  def __init__(self, client_id, client_secret):
    self.client_id = client_id
    self.client_secret = client_secret
    self.auth_token = self.get_auth_token()

  def get_auth_token(self):
    # Step 1 - Authorization 
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{self.client_id}:{self.client_secret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']

    return token


