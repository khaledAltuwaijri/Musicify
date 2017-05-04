from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^add_to_playlist$', add_to_playlist, name="add_to_playlist"),
    url(r'^show_playlists$', show_playlists, name="show_playlists"),
    url(r'^create_playlist$', create_playlist, name="create_playlist"),
    url(r'^view_playlist/(?P<playlist_id>\d+)/$', view_playlist, name="view_playlist"),
    url(r'^edit_playlist/(?P<playlist_id>\d+)/$', edit_playlist, name="edit_playlist"),
    url(r'^update_playlist/(?P<playlist_id>\d+)/$', update_playlist, name="update_playlist"),
    url(r'^remove_playlist/(?P<playlist_id>\d+)/$', remove_playlist, name="remove_playlist"),
    url(r'^remove_song/(?P<song_id>\d+)/(?P<playlist_id>\d+)/$', remove_song, name="remove_song"),
]
