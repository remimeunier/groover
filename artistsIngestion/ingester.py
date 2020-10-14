from api.models import Artist
from artistsIngestion.spotifyApi import SpotifyApi

class Reached(Exception): pass

def update_artists():
    spotify = SpotifyApi()

    try:
        # Fetch all new releases from spotify and iterate
        for release in spotify.get_new_release():
            # A release can have several artists colaborating, so iterate on artist per release
            for artist in release['artists']:
                # If an artist with current release exist we can stop fetching
                if Artist.objects.filter(name=artist['name'], last_release_name=release['name']).exists():
                    raise Reached
                # Check if this artist exists already in base
                in_base_artist = Artist.objects.filter(name=artist['name']).first()
                # If yes : update the last release values
                if in_base_artist is not None:
                    in_base_artist.last_release_name = release['name']
                    in_base_artist.last_release_date = release['release_date']
                    in_base_artist.save()
                # if not : create it
                else:
                    artist = spotify.get_artist(artist['id'])
                    Artist(name=artist['name'], last_release_name=release['name'],
                           last_release_date=release['release_date'],
                           spotify_link=artist['external_urls']['spotify']).save()
    except Reached:
      pass # stop everything if we reached an already ingested release

