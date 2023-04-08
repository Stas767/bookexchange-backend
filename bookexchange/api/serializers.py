from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Author, Book, BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    book_cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    favorites = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "subway",
            "exchange",
            "is_active",
            "date_joined",
            "book_cards",
            "favorites",
        )


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "patronymic",
            "bio",
            "books",
        )


class GenreSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ("id", "name", "slug", "books")


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    book_cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "pub_date",
            "last_update",
            "title",
            "description",
            "cover",
            "authors",
            "genres",
            "isbn",
            "year",
            "num_of_pages",
            "book_cards",
        )


class BookCardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(read_only=True)
    favorites = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BookCard
        fields = (
            "id",
            "pub_date",
            "last_update",
            "owner",
            "title",
            "description",
            "image",
            "book",
            "condition",
            "favorites",
        )


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ("id", "user", "book_card")
