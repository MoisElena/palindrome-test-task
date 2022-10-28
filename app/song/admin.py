from django.contrib import admin
from .models import Artist, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "artist",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("name", "song_number", "album",)
