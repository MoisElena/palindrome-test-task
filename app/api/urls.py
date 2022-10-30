from django.urls import path, include
from rest_framework import routers
from api.views import ArtistViewSet, AlbumViewSet, SongViewSet, CatalogViewSet

router = routers.SimpleRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'song', SongViewSet)
router.register(r'catalog', CatalogViewSet)



urlpatterns = [
    path('', include(router.urls)),
]