from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, related_name='albums')
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs')
    title = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fan(models.Model):
    user = models.ForeignKey(User, related_name='favorite_artists')
    artist = models.ForeignKey(Artist, related_name='fans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
