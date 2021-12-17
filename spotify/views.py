from django.shortcuts import render
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
# This is a bad thing and I don't want to fix it, to do so, enter commands:
# export SPOTIFY_CLIENT_ID = ... and export SPOTIFY_CLIENT_SECRET = ... into console
# for a windows machine, instead of export use SET
os.environ['SPOTIPY_CLIENT_ID'] = 'e0901fde975e48e0bb675d92fa675ac1'
os.environ['SPOTIPY_CLIENT_SECRET'] = '3feb3f65bb6b4e5c993736ec778bbfa5'
os.environ['SPOTIPY_REDIRECT_URL'] = 'https://127.0.0.1:8080/spotify'
# Create your views here.
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def index(request):

    if request.method == 'POST':
        artist = request.POST.get('artist', '')
        song = request.POST.get('song', '')

        if song is not '' and artist is not '':
            search = spotify.search(q='artist:' + artist + ' track:' + song, limit=1)
        elif artist is not '':
            search = spotify.search(q='artist:' + artist, limit=10)
        else:
            search = spotify.search(q='track:' + song, limit=10)

        return render(request, 'spotify/index.html', {'search': search, 'artist': artist})
    else:
        artist = 'Imagine Dragons'
        search = spotify.search(q='artist:' + artist, limit=10)
        return render(request, 'spotify/index.html', {'search': search, 'artist': artist})