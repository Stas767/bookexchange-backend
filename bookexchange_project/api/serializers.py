from rest_framework import serializers
from djoser.serializers import UserSerializer

from users.models import User
from books.models import BookCard, Favorites


# Для Стаса: не стал убирать эти неактуальные сериализаторы, просто их закоментил. Мало ли прогодятся шаблоны по быстрому.


# class CustomUserSerializer(UserSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'email', 'username')

# class PubAuthorSerializer(serializers.ModelSerializer):
#     books = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = PubAuthor
#         fields = ('id', 'username', 'books')
#         ref_name = 'ReadOnlyUsers'


# class BookAuthorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = BookAuthor
#         fields = ('__all__')


# class GenreSerializer(serializers.ModelSerializer):
#     genre = serializers.CharField(source='genre_title')

#     class Meta:
#         model = Genre
#         fields = ('id', 'genre')


# class BookSerializer(serializers.ModelSerializer):
#     pub_author = serializers.SlugRelatedField(
#         slug_field='username',
#         read_only=True
#     )
#     book_author = serializers.StringRelatedField()
#     genre = GenreSerializer(many=True, required=False)

#     class Meta:
#         fields = '__all__'
#         model = Book
