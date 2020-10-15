import pytest
from rest_framework import status
from unittest.mock import Mock, patch

from api.tests.factory import request_factory
from spotifyAuth.models import SpotifyAuth
from spotifyAuth.views import SpotifyAuthView
from spotifyAuth.spotifyAuthApi import ErrorWhileGettingToken

class TestSpotifyAuthView:

    @pytest.mark.django_db
    def test_callback_no_code(self, request_factory):
        request = request_factory.get('auth/callback')
        view = SpotifyAuthView.as_view()
        response = view(request)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_callback_succes(self, request_factory):
        mock_API = Mock()
        mock_API.getUserToken.return_value = { 'access_token': 'some', 'refresh_token': 'thing' }
        request = request_factory.get('artists?code=5656')
        view = SpotifyAuthView.as_view()
        with patch('spotifyAuth.spotifyAuthApi.SpotifyAuthApi.__new__', return_value=mock_API):
            response = view(request)
        a =  SpotifyAuth.objects.all().first()
        assert a.token == 'some'

    @pytest.mark.django_db
    def test_error_token(self, request_factory):
        request = request_factory.get('artists?code=5656')
        view = SpotifyAuthView.as_view()
        with patch('spotifyAuth.spotifyAuthApi.SpotifyAuthApi.__new__', side_effect=ErrorWhileGettingToken):
            response = view(request)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

