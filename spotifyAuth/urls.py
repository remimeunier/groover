from django.urls import include, path

from .views import SpotifyAuthView


urlpatterns = [
    path("callback", SpotifyAuthView.as_view(), name="spotify_auth"),
]
