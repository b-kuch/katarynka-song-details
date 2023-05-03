import json

from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name : "str" = models.CharField(max_length=300)

    def __str__(self):
        return self.artist_name

    def identifier(self) -> str:
        return f"{self.artist_name}"

    def toDict(self):
        return {
            "name": self.artist_name,
            "identifier": self.identifier()
        }


class Album(models.Model):
    album_name : "str" = models.CharField(max_length=300)
    artist : "Artist" = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.album_name}"

    def identifier(self) -> str:
        return f"{self.artist.artist_name}-{self.album_name}"

    def toDict(self):
        return {
            "album": self.album_name,
            "identifier": self.identifier()
        }


class Song(models.Model):
    song_name : "str" = models.CharField(max_length=300)
    artist : "Artist" = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album : "Album" = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.song_name}"

    def identifier(self) -> str:
        return f"{self.artist.artist_name}-{self.album.album_name}-{self.song_name}"

    def filename(self) -> str:
        return f"{self.artist.artist_name} - {self.song_name}.mp3"

    def toDict(self):
        return {
            "song_name": self.song_name,
            "artist": self.artist.toDict(),
            "album": self.album.toDict(),
            "filename": self.filename(),
            "identifier": self.identifier()
        }
