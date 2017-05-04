from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^search$', search, name="search"),
    url(r'^add_artist_page$', add_artist_page, name="add_artist_page"),
    url(r'^add_artist$', add_artist, name="add_artist"),
    url(r'^songs/(?P<album_id>\d+)/$', songs, name="songs"),
    url(r'^add_song/(?P<album_id>\d+)/$', add_song, name="add_song"),
    url(r'^remove_song/(?P<song_id>\d+)/(?P<album_id>\d+)/$', remove_song, name="remove_song"),
]
