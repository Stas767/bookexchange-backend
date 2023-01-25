# Для Стаса: тут тоже все закомментировал. Мало ли пригодится прям тут.


# from books.models import BookAuthor, Book, Genre
from users.models import User
from rest_framework import viewsets, permissions, filters

# from .serializers import (
#     BookSerializer,
#     BookAuthorSerializer,
#     GenreSerializer
# )
from api.permissions import IsAuthorOrReadOnly


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]
#     filter_backends = (filters.SearchFilter,)
#     search_fields = (
#         'author__last_name',
#         'author__first_name',
#         'title',
#         'creation_date',
#         )


# class BookAuthorViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = BookAuthor.objects.all()
#     serializer_class = BookAuthorSerializer


# class GenreViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
