import pytest
from django.conf import settings
from rest_framework import status
from unittest.mock import Mock, patch

from spotifyAuth.models import SpotifyAuth
from spotifyAuth.spotifyAuthApi import SpotifyAuthApi, ErrorWhileGettingToken

class TestSpotifyAuthApi:

    @pytest.mark.django_db
    def test_find_token(self):
        mock_response = Mock()
        mock_response.json.return_value = { 'access_token': 'some', 'refresh_token': 'thing' }
        with patch('requests.post', return_value=mock_response):
            token = SpotifyAuthApi().getUserToken('SOME CODE')
        assert token['access_token'] == 'some'
        assert token['refresh_token'] == 'thing'

    @pytest.mark.django_db
    def test_refresh_token(self):
        mock_response = Mock()
        mock_response.json.return_value = { 'access_token': 'some', 'refresh_token': 'thing' }
        with patch('requests.post', return_value=mock_response):
            token = SpotifyAuthApi().refreshAuth('thing')
        assert token['refresh_token'] == 'thing'

    @pytest.mark.django_db
    def test_redirection_uri(self):
        assert SpotifyAuthApi().getUser() == "https://accounts.spotify.com/authorize/?client_id={}&redirect_uri=http://localhost:5000/auth/callback&scope=user-read-email user-read-private&response_type=code".format(settings.SPOTIFY_CLIENT_ID)
