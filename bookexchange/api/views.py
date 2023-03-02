from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import BookCardSerializer, FavoritesSerializer
from books.models import BookCard, Favorites


class BookCardViewSet(ReadOnlyModelViewSet):
    queryset = (
        BookCard.objects.select_related('owner')
        .prefetch_related('author', 'genre')
    )
    serializer_class = BookCardSerializer


class FavoritesViewSet(ReadOnlyModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
