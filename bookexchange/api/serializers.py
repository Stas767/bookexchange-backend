from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Author, BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'subway', 'exchange', )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name', 'surname', 'last_name', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', )


class BookCardSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = BookCard
        fields = (
            'id', 'pub_date', 'owner', 'title', 'description', 'image',
            'author', 'genre', 'isbn', 'condition', 'year', 
        )


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('user', 'book_card', )
