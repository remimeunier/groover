import pytest

from datetime import datetime, timezone, timedelta

from api.models import Artist, Genre

@pytest.fixture
def artists_with_genre(db):
    genre1 = Genre(name='pop')
    genre2 = Genre(name='rap')
    genre3 = Genre(name='rock')
    genre1.save()
    genre2.save()
    genre3.save()
    a2 = Artist(name='Someone Famous', last_release_name='Best Stuf',
               last_release_date=datetime.now(timezone.utc) - timedelta(days=1),
               spotify_link='and URI')
    a1 = Artist(name='an other person', last_release_name='Second best stuff',
               last_release_date=datetime.now(timezone.utc),
               spotify_link='and URI2')
    a1.save()
    a2.save()
    a1.genres.set([genre1, genre2])
    a2.genres.set([genre2, genre3])
    a1.save()
    a2.save()
    return [a1, a2]
