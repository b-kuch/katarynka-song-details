from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=300)


class Album(models.Model):
    album_name = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    song_name = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
