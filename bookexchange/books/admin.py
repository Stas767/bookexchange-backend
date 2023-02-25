from django.contrib import admin

from books.models import Advert, Author, Book, BookCard, Favorites, Genre

admin.site.register(Advert)
admin.site.register(Book)
admin.site.register(BookCard)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Favorites)
