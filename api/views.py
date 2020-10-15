from django.shortcuts import redirect
from rest_framework import generics

from spotifyAuth.models import SpotifyAuth
from spotifyAuth.spotifyAuthApi import SpotifyAuthApi
from .models import Artist
from .serializers import ArtistSerializer

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.order_by('-last_release_date').all()
    serializer_class = ArtistSerializer

    def list(self, request):
        if SpotifyAuth.objects.all().first():
            return super().list(request)
        else:
            # redirect to the spotify auth page
            return redirect(SpotifyAuthApi().getUser())
