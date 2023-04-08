from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (
    AuthorSerializer,
    BookCardSerializer,
    BookSerializer,
    FavoritesSerializer,
    GenreSerializer,
)
from books.models import Author, Book, BookCard, Favorites, Genre


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCardViewSet(viewsets.ModelViewSet):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializer

    @swagger_auto_schema(request_body=no_body)
    @action(detail=True, methods=["post"])
    def favorite(self, request, pk=None):
        instance = self.get_object()
        user = request.user
        _, _ = Favorites.objects.get_or_create(user=user, book_card=instance)
        return Response(
            self.get_serializer(instance=instance).data,
            status=status.HTTP_201_CREATED,
        )

    @favorite.mapping.delete
    def delete_favorite(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        favorite = get_object_or_404(Favorites, user=user, book_card=instance)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
