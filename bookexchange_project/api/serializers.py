# не знаю что это такое, пока оставляю
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.models import BookCard


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'city', 'exchange')


class BookCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookCard
        fields = (
            'id', 'publisher', 'book_title',
            'author_name', 'genre', 'book_description',
            'book_image', 'isbn', 'condition', 'year'
        )
