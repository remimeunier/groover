from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView

from api.utils import build_error_response
from spotifyAuth.models import SpotifyAuth
from spotifyAuth.spotifyAuthApi import SpotifyAuthApi, ErrorWhileGettingToken

class SpotifyAuthView(APIView):

    def get(self, request):
        code = request.GET.get('code', None)
        if code is None:
            return build_error_response(status.HTTP_401_UNAUTHORIZED, 'You need to grant access to continue')
        try:
            tokens = SpotifyAuthApi().getUserToken(code)
        except ErrorWhileGettingToken:
            return build_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Something went wrong, try later')

        SpotifyAuth(token=tokens['access_token'], refresh_token=tokens['refresh_token']).save()
        return redirect('api/artists')

