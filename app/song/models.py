from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    artist = models.ForeignKey(
        "Artist", 
        on_delete=models.PROTECT, 
        verbose_name="Artist", 
        related_name="album"
    )
    
    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    name = models.TextField()
    song_number = models.IntegerField()
    album = models.ForeignKey(
        "Album",
        on_delete=models.PROTECT,
        verbose_name="Album",
        related_name="song"
    )
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ('name', 'album')
