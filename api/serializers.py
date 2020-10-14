# serializers.py
from rest_framework import serializers

from .models import Artist, Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'last_release_name', 'last_release_date', 'spotify_link', 'genres')
