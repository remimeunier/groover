from rest_framework import generics

from .models import Artist
from .serializers import ArtistSerializer

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
