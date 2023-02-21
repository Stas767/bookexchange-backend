# не знаю что это такое, пока оставляю
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import BookCard, Favorites
from users.models import User


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


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('book_card', 'user')
