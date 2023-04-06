from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Author, Book, BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    # book_cards = serializers.RelatedField(read_only=True, many=True)
    # favorites = serializers.RelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
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
    # books = serializers.RelatedField(read_only=True, many=True)

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "bio",
            "books",
        )


class GenreSerializer(serializers.ModelSerializer):
    # books = serializers.RelatedField(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = ("name", "slug", "books")


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(read_only=True, many=True)
    # genres = GenreSerializer(read_only=True, many=True)
    # book_cards = serializers.RelatedField(read_only=True, many=True)

    class Meta:
        model = Book
        fields = (
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
    # owner = CustomUserSerializer(read_only=True)
    # book = BookSerializer(read_only=True)
    # favorites = serializers.RelatedField(read_only=True, many=True)

    class Meta:
        model = BookCard
        fields = (
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
        fields = ("user", "book_card")
