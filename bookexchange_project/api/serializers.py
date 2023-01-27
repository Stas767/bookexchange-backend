from rest_framework import serializers
# не знаю что это такое, пока оставляю
from djoser.serializers import UserSerializer

from users.models import User
from books.models import BookCard, Favorites


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
