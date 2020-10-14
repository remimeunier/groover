import pytest
from unittest.mock import Mock, patch

from api.models import Artist, Genre
from artistsIngestion import ingester
from artistsIngestion.ingester import Reached
from artistsIngestion.tests.fixtures import (
    news_release_from_spotify,
    artist_from_spotify,
    band_of_horses_artist
)


class TestIngester:

    @pytest.mark.django_db
    def test_update_artists(self, capfd, news_release_from_spotify, artist_from_spotify):
        mock_API = Mock()
        mock_API.get_new_release.return_value = news_release_from_spotify
        mock_API.get_artist.return_value = artist_from_spotify
        with patch('artistsIngestion.spotify.SpotifyApi.__new__', return_value=mock_API):
            ingester.update_artists()
        assert Artist.objects.filter(name="Band of Horses").exists()
        assert Genre.objects.filter(name="indie pop").exists()
        assert Genre.objects.filter(name="indie folk").exists()
        with patch('artistsIngestion.spotify.SpotifyApi.__new__', return_value=mock_API):
            ingester.update_artists()
        out, err = capfd.readouterr()
        assert out == "reached\n"

    @pytest.mark.django_db
    def test_update_artists_last_release(self, news_release_from_spotify, artist_from_spotify,
                                         band_of_horses_artist):
        last_release_name = band_of_horses_artist.last_release_name
        mock_API = Mock()
        mock_API.get_new_release.return_value = news_release_from_spotify
        mock_API.get_artist.return_value = artist_from_spotify
        with patch('artistsIngestion.spotify.SpotifyApi.__new__', return_value=mock_API):
            ingester.update_artists()
        a = Artist.objects.filter(name="Band of Horses").first()
        assert a.last_release_name != last_release_name

