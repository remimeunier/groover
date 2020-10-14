import pytest
from rest_framework import status
from api.tests.factory import request_factory
from api.tests.fixtures import artists_with_genre
from api.views import ArtistList

class TestArtistList:

    @pytest.mark.django_db
    def test_artist_list_success(self, request_factory, artists_with_genre):
        request = request_factory.get('artists')
        view = ArtistList.as_view()
        response = view(request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['name'] == artists_with_genre[0].name
        assert response.data[1]['name'] == artists_with_genre[1].name
