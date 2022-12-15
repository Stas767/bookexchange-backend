from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField
# from rest_framework.validators import UniqueTogetherValidator
# from djoser.serializers import UserSerializer

from books.models import Book, BookAuthor, Genre, PubAuthor


# class CustomUserSerializer(UserSerializer):

#     class Meta:
#         model = User
#         fields = ('email', 'id', 'username', 'first_name', 'last_name')

class PubAuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = PubAuthor
        fields = ('id', 'username', 'username', 'books', 'birth_date')
        ref_name = 'ReadOnlyUsers'


class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre_title')

    class Meta:
        model = Genre
        fields = ('id', 'genre')


class BookSerializer(serializers.ModelSerializer):
    pub_author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    book_author = serializers.StringRelatedField()
    genre = GenreSerializer(many=True, required=False)

    class Meta:
        fields = '__all__'
        model = Book
