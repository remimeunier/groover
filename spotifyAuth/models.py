from django.db import models

from spotifyAuth.spotifyAuthApi import SpotifyAuthApi


class SpotifyAuth(models.Model):
    token = models.TextField()
    refresh_token = models.TextField()

    def refresh_tokens(self):
        tokens = SpotifyAuthApi().refreshAuth(self.refresh_token)
        self.token = tokens['access_token']
        self.save()
        return self

