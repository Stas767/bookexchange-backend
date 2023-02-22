from rest_framework import viewsets

from books.models import BookCard
from .serializers import BookCardSerializers


class BookCardViewSet(viewsets.ModelViewSet):
    queryset = BookCard.objects.all()
    serializer_class = BookCardSerializers
