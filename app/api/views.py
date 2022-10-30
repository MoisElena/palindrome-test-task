from rest_framework import viewsets
from rest_framework.decorators import action
from song.models import Artist, Album, Song
from api.serializers import (ArtistSerializer, AlbumSerializer,
                             SongSerializer, CatalogSerializer,
                             AlbumOfArtistSerializer, AlbumAndSongSerializer)

class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    
    @action(detail=True, methods=['get'], url_path='album')
    def get_album_of_artist(self, request, *args, **kwargs):
        self.serializer_class = AlbumOfArtistSerializer
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
    @action(detail=True, methods=['get'], url_path='song')
    def get_song_of_album(self, request, *args, **kwargs):
        self.serializer_class = AlbumAndSongSerializer
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Artist.objects.all()
