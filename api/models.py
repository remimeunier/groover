from datetime import date
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    last_release_name = models.CharField(max_length=100, default='Non Specified')
    last_release_date = models.DateTimeField(default=date.today)
    genres = models.ManyToManyField(Genre, blank=True, related_name='artists')
    spotify_link = models.CharField(max_length=200, default='Non Specified')

    def __str__(self):
        return self.name
