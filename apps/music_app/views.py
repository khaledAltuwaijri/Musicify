from django.shortcuts import render, redirect, HttpResponse, reverse
import re
from django.contrib import messages
from .models import Album, Artist, Song, Fan
from ..playlist_app.models import Playlist, Addition, Listener

# Create your views here.
def index(request):
    return render(request, 'music_app/index.html')

def add_artist_page(request):
    context = {
        "artists": Artist.objects.all().order_by('-created_at'),
    }
    return render(request, 'music_app/add_artist.html', context)

def add_artist(request):
    if request.method == "POST":
        try:
            artist = Artist.objects.create(name=request.POST['artist_name'])
            album = Album.objects.create(title=request.POST['album_name'], year=request.POST['album_year'], artist=artist)
        except:
            artist = Artist.objects.get(name=request.POST['artist_name'])
            album = Album.objects.create(title=request.POST['album_name'], year=request.POST['album_year'], artist=artist)
    return redirect('music:add_artist_page')

def songs(request, album_id):
    context = {
        "songs": Song.objects.filter(album_id = album_id).order_by('-created_at'),
        "album": Album.objects.get(id = album_id),
        "playlists": Playlist.objects.all(),
    }
    return render(request, 'music_app/songs.html', context)

def add_song(request, album_id):
    if request.method == "POST":
        song = Song.objects.create(title=request.POST['song_title'], genre=request.POST['song_genre'], album_id=album_id)
    return redirect(reverse('music:songs', kwargs={"album_id": album_id}))

def remove_song(request, song_id, album_id):
    song = Song.objects.get(id=song_id).delete()
    return redirect(reverse('music:songs', kwargs={"album_id": album_id}))

def search(request):
    if request.method=="POST":
        search_query = request.POST['search_query']
        try:
            songs = Song.objects.filter(title__contains = search_query)
            albums = Album.objects.filter(title__contains = search_query)
            artists = Artist.objects.filter(name__contains = search_query)
        except:
            messages.error(request, 'NO SEARCH RESULTS!! PLEASE TRY AGAIN')
            return redirect('playlists:home')
        context = {
            "songs": songs,
            "albums": albums,
            "artists": artists,
        }
    return render(request, 'music_app/search_results.html', context)
