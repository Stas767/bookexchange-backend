from rest_framework.viewsets import ReadOnlyModelViewSet

from api_versions.serializers import (BookSerializerV2, BookCardSerializerV1,
                                      BookCardSerializerV2,
                                      FavoritesSerializerV1)
from books.models import Book, BookCard, Favorites


class BookCardViewSetV1(ReadOnlyModelViewSet):
    queryset = (
        BookCard.objects.select_related('owner')
        .prefetch_related('author', 'genre')
    )
    serializer_class = BookCardSerializerV1


class FavoritesViewSetV1(ReadOnlyModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializerV1


class BookViewSetV2(ReadOnlyModelViewSet):
    queryset = (
        Book.objects.prefetch_related('authors', 'genres')
    )
    serializer_class = BookSerializerV2


class BookCardViewSetV2(ReadOnlyModelViewSet):
    queryset = (
        BookCard.objects.select_related('owner')
        .prefetch_related('author', 'genre')
    )
    serializer_class = BookCardSerializerV2
