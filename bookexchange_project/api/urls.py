from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import get_doc_shema_view
from api.views import (AdvertViewSet, AuthorViewSet, BookViewSet,
                       FavoritesViewSet, GenreViewSet)

router = DefaultRouter()
router.register(r'adverts', AdvertViewSet)
router.register(r'athors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'favorites', FavoritesViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path(
        'docs/dynamic/', get_doc_shema_view().with_ui('redoc', cache_timeout=0)
    ),

    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
