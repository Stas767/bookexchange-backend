from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from api.serializers import BookCardSerializer, FavoritesSerializer
from books.models import BookCard, Favorites


def get_doc_shema_view():
    return get_schema_view(
        info=openapi.Info(
            title='Bookexchange API documentation',
            default_version='1',
            description='The first version of dynamic documentation',
            terms_of_service="https://localhost:8000/",
            contact=openapi.Contact(email="test@admin.ru"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )


class BookCardViewSet(ListModelMixin, RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializer


class FavoritesViewSet(ListModelMixin, RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
