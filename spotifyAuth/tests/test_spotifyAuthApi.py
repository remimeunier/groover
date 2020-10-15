import pytest
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
