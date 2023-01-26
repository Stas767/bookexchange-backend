from rest_framework import viewsets

from books.models import BookCard, Favorites
from .serializers import BookCardSerializers, FavoritesSerializer


class BookCardViewSet(viewsets.ModelViewSet):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializers


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
