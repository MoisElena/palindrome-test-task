from rest_framework import viewsets
from song.models import Artist, Album, Song
from api.serializers import ArtistSerializer, AlbumSerializer, SongSerializer, SongCatalogSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    
class SongCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SongCatalogSerializer
    queryset = Artist.objects.all()