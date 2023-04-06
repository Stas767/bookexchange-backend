from api.serializers import (
    AdvertSerializer,
    AuthorSerializer,
    BookCardSerializer,
    BookSerializer,
    FavoritesSerializer,
    GenreSerializer,
)
from books.models import Advert, Author, Book, BookCard, Favorites, Genre
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


def get_doc_shema_view():
    return get_schema_view(
        info=openapi.Info(
            title="Bookexchange API documentation",
            default_version="1",
            description="The first version of dynamic documentation",
            terms_of_service="https://localhost:8000/",
            contact=openapi.Contact(email="test@admin.ru"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class BookCardViewSet(
    ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class FavoritesViewSet(
    ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
