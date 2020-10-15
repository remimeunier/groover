import json, requests
from django.conf import settings

SPOTIFY_URL_NEW_RELEASE = "https://api.spotify.com/v1/browse/new-releases"
SPOTIFY_ARTIST_URL = "https://api.spotify.com/v1/artists/"


class SpotifyErrorMessage(Exception): pass

class SpotifyApi(object):

    def __init__(self, auth):
        self.auth = auth

    def get_new_release(self):
        new_releases = requests.get(SPOTIFY_URL_NEW_RELEASE, headers=self._headers()).json()
        if self._is_token_expired(new_releases):
            self._handle_token_expired()
            return self.get_new_release()
        return new_releases['albums']['items']

    def get_artist(self, spotify_artist_id):
        artist = requests.get(SPOTIFY_ARTIST_URL + spotify_artist_id, headers=self._headers()).json()
        if self._is_token_expired(artist):
            self._handle_token_expired()
            return self.get_artist(spotify_artist_id)
        return artist

    def _headers(self):
        return { 'Authorization': 'Bearer {token}'.format(token=self.auth.token) }

    def _handle_token_expired(self):
        self.auth = self.auth.refresh_tokens()

    def _is_token_expired(self, response):
        if "error" in response:
            if response['error']['message'] == 'The access token expired':
                return True
            else:
                raise SpotifyErrorMessage
        return False
