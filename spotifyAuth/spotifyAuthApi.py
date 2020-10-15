import base64, json, requests, os
from django.conf import settings

class ErrorWhileGettingToken(Exception): pass

class SpotifyAuthApi(object):
    SPOTIFY_URL_AUTH = "https://accounts.spotify.com/authorize/"
    SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token/"
    RESPONSE_TYPE = "code"
    HEADER = "application/x-www-form-urlencoded"
    CLIENT_ID = settings.SPOTIFY_CLIENT_ID
    CLIENT_SECRET = settings.SPOTIFY_CLIENT_SECRET
    CALLBACK_URL = "http://localhost:5000/auth"
    SCOPE = "user-read-email user-read-private"

    def getUser(self):
        return self._getAuth(f"{self.CALLBACK_URL}/callback", self.SCOPE)

    def getUserToken(self, code):
        return self._getToken(code, f"{self.CALLBACK_URL}/callback")

    def refreshAuth(self, refresh_token):
        body = {"grant_type": "refresh_token", "refresh_token": refresh_token}

        post = requests.post(
            self.SPOTIFY_URL_TOKEN, data=body, headers=self._headers()
        ).json()
        return self._handleToken(post)

    def _getAuth(self, redirect_uri, scope):
        return (
            f"{self.SPOTIFY_URL_AUTH}"
            f"?client_id={self.CLIENT_ID}"
            f"&redirect_uri={redirect_uri}"
            f"&scope={scope}"
            "&response_type=code"
        )

    def _getToken(self, code, redirect_uri):
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
        }

        post = requests.post(self.SPOTIFY_URL_TOKEN, params=body, headers=self._headers()).json()
        return self._handleToken(post)

    def _headers(self):
        encoded = base64.b64encode(f"{self.CLIENT_ID}:{self.CLIENT_SECRET}".encode()).decode()
        return {
            "Content-Type": self.HEADER,
            "Authorization": f"Basic {encoded}",
        }

    def _handleToken(self, response):
        if "error" in response:
            raise ErrorWhileGettingToken
        return response
