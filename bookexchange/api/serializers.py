from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import BookCard, Favorites, Genre

User = get_user_model()


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'subway', 'exchange', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', )


class BookCardSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    owner = CustomUserSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = BookCard
        fields = (
            'id', 'pub_date', 'owner', 'title', 'description', 'image',
            'author', 'genre', 'isbn', 'condition', 'year', 
        )
    
    def get_author(self, instance):
        return ', '.join([str(author) for author in instance.author.all()])


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('user', 'book_card', )
