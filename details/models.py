from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=300)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.album_name}"

    def identifier(self) -> str:
        return f"{self.artist}_{self.album_name}"


class Song(models.Model):
    song_name = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.song_name}"

    def identifier(self) -> str:
        return f"{self.artist}_{self.album_name}_{self.song_name}"
