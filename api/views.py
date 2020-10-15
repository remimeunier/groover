from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.views import APIView

from .models import Artist, SpotifyAuth
from .serializers import ArtistSerializer
from artistsIngestion.spotifyAuth import SpotifyAuthApi

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.order_by('-last_release_date').all()
    serializer_class = ArtistSerializer

    def list(self, request):
        if SpotifyAuth.objects.all().first():
            return super().list(request)
        else:
            return redirect(SpotifyAuthApi().getUser())


class SpotifyAuthView(APIView):

    def get(self, request):
        print(request)

