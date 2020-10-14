import base64, json, requests, os
from django.conf import settings

SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token/"
SPOTIFY_URL_NEW_RELEASE = "https://api.spotify.com/v1/browse/new-releases"
SPOTIFY_ARTIST_URL = "https://api.spotify.com/v1/artists/"
HEADER = "application/x-www-form-urlencoded"
CLIENT_ID = settings.SPOTIFY_CLIENT_ID
CLIENT_SECRET = settings.SPOTIFY_CLIENT_SECRET

class SpotifyApi(object):

    def __init__(self):
        self.token = self._getToken()

    def _getToken(self):
        auth_response = requests.post(SPOTIFY_URL_TOKEN, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })

        return auth_response.json()['access_token']

    def get_new_release(self):
        new_releases = requests.get(SPOTIFY_URL_NEW_RELEASE, headers=self._headers())
        return new_releases.json()['albums']['items']

    def get_artist(self, spotify_artist_id):
        artist = requests.get(SPOTIFY_ARTIST_URL + spotify_artist_id, headers=self._headers())
        return artist.json()

    def _headers(self):
        return { 'Authorization': 'Bearer {token}'.format(token=self.token) }
