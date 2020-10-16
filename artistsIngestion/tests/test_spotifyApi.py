import pytest
from unittest.mock import Mock, patch

from api.tests.fixtures import dummy_auth
from spotifyAuth.models import SpotifyAuth
from artistsIngestion.spotifyApi import SpotifyApi, SpotifyErrorMessage
from artistsIngestion.tests.fixtures import (
    news_release_from_spotify,
    artist_from_spotify,
)

class TestSpotifyApi:

    @pytest.mark.django_db
    def test_get_new_release(self, dummy_auth, news_release_from_spotify):
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, dummy_auth)
        mock_response = Mock()
        mock_response.json.return_value = { 'albums': { 'items': news_release_from_spotify } }
        with patch('requests.get', return_value=mock_response):
            result = api.get_new_release()
        assert result == news_release_from_spotify

    @pytest.mark.django_db
    def test_get_artist(self, dummy_auth, artist_from_spotify):
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, dummy_auth)
        mock_response = Mock()
        mock_response.json.return_value = artist_from_spotify
        with patch('requests.get', return_value=mock_response):
            result = api.get_artist('id')
        assert result == artist_from_spotify

    @pytest.mark.django_db
    def test_spotify_error_on_artist(self, dummy_auth):
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, dummy_auth)
        mock_response = Mock()
        mock_response.json.return_value = { 'error': { 'message' : 'Not available' } }
        with patch('requests.get', return_value=mock_response):
            with pytest.raises(SpotifyErrorMessage):
                result = api.get_artist('id')

    @pytest.mark.django_db
    def test_spotify_error_on_release(self, dummy_auth):
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, dummy_auth)
        mock_response = Mock()
        mock_response.json.return_value = { 'error': { 'message' : 'Not available' } }
        with patch('requests.get', return_value=mock_response):
            with pytest.raises(SpotifyErrorMessage):
                result = api.get_new_release()

    @pytest.mark.django_db
    def test_get_new_release_with_token_changes(self, news_release_from_spotify):
        mock_auth = Mock()
        mock_auth.token.return_value = 'something'
        mock_auth._handle_token_expired.return_value = mock_auth
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, mock_auth)
        mock_response = Mock()
        mock_response.json.side_effect = [ { 'error': { 'message' : 'The access token expired' } },
                                           { 'albums': { 'items': news_release_from_spotify } } ]
        with patch('requests.get', return_value=mock_response):
            result = api.get_new_release()
        assert result == news_release_from_spotify

    @pytest.mark.django_db
    def test_get_artist_with_token_changes(self, artist_from_spotify):
        mock_auth = Mock()
        mock_auth.token.return_value = 'something'
        mock_auth._handle_token_expired.return_value = mock_auth
        api =  object.__new__(SpotifyApi)
        SpotifyApi.__init__(api, mock_auth)
        mock_response = Mock()
        mock_response.json.side_effect = [ { 'error': { 'message' : 'The access token expired' } },
                                           artist_from_spotify ]
        with patch('requests.get', return_value=mock_response):
            result = api.get_artist('id')
        assert result == artist_from_spotify
