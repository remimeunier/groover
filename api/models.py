from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    last_release_name = models.CharField(max_length=100)
    last_release_date = models.DateTimeField()
    genres = models.ManyToManyField(Genre, blank=True, related_name='artists')
    spotify_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
