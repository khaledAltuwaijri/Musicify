from django.shortcuts import render, redirect, HttpResponse, reverse
import re
from django.contrib import messages
from .models import Playlist, Addition, Listener
from ..music_app.models import Song, Artist, Album

# Create your views here.
def index(request):
    context = {
        "songs": Song.objects.all()[:5].filter(),
        "playlists": Playlist.objects.all()[:5].filter(),
        "artists": Artist.objects.all()[:5].filter()
    }
    return render(request, 'playlist_app/index.html', context)

def add_to_playlist(request):
    if request.method == "POST":
        song_id = request.POST['song_id']
        playlist_id = request.POST['playlist_id']
    Addition.objects.create(song_id = song_id, playlist_id = playlist_id)
    return redirect('playlists:show_playlists')

def show_playlists(request):
    context = {
        "playlists": Playlist.objects.all()
    }
    return render(request, 'playlist_app/playlists.html', context)

def create_playlist(request):
    if request.method =='POST':
        playlist = Playlist.objects.create(title=request.POST['playlist_name'], description=request.POST['playlist_description'])
    return redirect('playlists:show_playlists')

def view_playlist(request, playlist_id):
    context = {
        "songs": Song.objects.filter(playlists__playlist_id=playlist_id),
        "playlist": Playlist.objects.get(id=playlist_id)
    }
    return render(request, 'playlist_app/view_playlist.html', context)

def edit_playlist(request, playlist_id):
    context = {
        "playlist": Playlist.objects.get(id=playlist_id)
    }
    return render(request, 'playlist_app/edit_playlist.html', context)

def update_playlist(request, playlist_id):
    if request.method=='POST':
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            playlist.title = request.POST['playlist_title']
            playlist.description = request.POST['playlist_description']
            playlist.save()
            return redirect(reverse('playlists:view_playlist', kwargs={"playlist_id":playlist.id}))
        except:
            message.error(request, 'Inputs not valid, try again!')
            return redirect('playlists:edit_playlist')
    else:
        return redirect('playlists:edit_playlist')

def remove_playlist(request, playlist_id):
    Playlist.objects.get(id=playlist_id).delete()
    return redirect('playlists:show_playlists')

def remove_song(request, song_id, playlist_id):
    Addition.objects.get(song_id=song_id).delete()
    return redirect(reverse('playlists:view_playlist', kwargs={"playlist_id": playlist_id}))
