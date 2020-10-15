from django.urls import include, path

from .views import ArtistList, SpotifyAuthView


urlpatterns = [
    path("artists/", ArtistList.as_view(), name="artists_list"),
]
