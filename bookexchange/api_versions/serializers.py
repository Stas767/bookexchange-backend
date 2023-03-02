from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Author, Book, BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializerV1(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'subway', 'exchange', )


class AuthorSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name', 'surname', 'last_name', )


class GenreSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', )


class FavoritesSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('user', 'book_card', )


class BookCardSerializerV1(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    owner = CustomUserSerializerV1()
    genre = GenreSerializerV1(many=True)

    class Meta:
        model = BookCard
        fields = (
            'id', 'pub_date', 'owner', 'title', 'description', 'image',
            'author', 'genre', 'isbn', 'condition', 'year', 
        )
    
    def get_author(self, instance):
        return ', '.join([str(author) for author in instance.author.all()])


class BookSerializerV2(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_authors(self, instance):
        return ', '.join([str(author) for author in instance.authors.all()])
    
    def get_genres(self, instance):
        return ', '.join([str(genre) for genre in instance.genres.all()])


class BookCardSerializerV2(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.email")
    book = BookSerializerV2()

    class Meta:
        model = BookCard
        fields = (
            'id', 'pub_date', 'owner', 'title', 'description', 'image',
            'book', 'condition'
        )
