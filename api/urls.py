from django.urls import include, path

from .views import ArtistList


urlpatterns = [
    path("artists/", ArtistList.as_view(), name="artists_list"),
]
