# serializers.py
from rest_framework import serializers

from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'last_release_name', 'last_release_date', 'spotify_link')
