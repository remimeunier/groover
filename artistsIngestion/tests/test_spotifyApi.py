# import pytest
# from unittest.mock import Mock, patch

# from spotifyAuth.models import SpotifyAuth
# from artistsIngestion.spotifyApi import SpotifyApi
# from artistsIngestion.tests.fixtures import (
#     news_release_from_spotify,
#     artist_from_spotify,
# )

# class TestSpotifyApi:

#     @pytest.mark.django_db
#     def test_get_new_release(self, artist_from_spotify, news_release_from_spotify):
#         spotify_auth = SpotifyAuth(token="something", refresh_token="refresh something")
#         spotify_auth.save()
#         api = SpotifyApi(auth=spotify_auth)
#         return_val = { 'albums': { 'items': news_release_from_spotify }}
#         with patch('requests.get', return_value=return_val):
#             result = api.get_new_release()
#         assert resul == news_release_from_spotify
