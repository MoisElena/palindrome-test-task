from django.contrib import admin
from .models import Artist, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "artist",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "song_number", "album",)
