from rest_framework import serializers
from song.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'artist']
        

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'song_number', 'album']


class AlbumAndSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'artist', 'song']
        

class AlbumOfArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'album']


class CatalogSerializer(serializers.ModelSerializer):
    album = AlbumAndSongSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'album']