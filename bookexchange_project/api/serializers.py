from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Advert, Author, Book, BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookCardSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = BookCard
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()
    book = BookSerializer()

    class Meta:
        model = Advert
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = '__all__'
