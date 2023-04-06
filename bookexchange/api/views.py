from api.serializers import (
    AuthorSerializer,
    BookCardSerializer,
    BookSerializer,
    FavoritesSerializer,
    GenreSerializer,
)
from books.models import Author, Book, BookCard, Favorites, Genre
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCardViewSet(viewsets.ModelViewSet):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializer


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
