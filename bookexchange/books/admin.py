from django.contrib import admin

from books.models import Author, BookCard, Favorites, Genre

admin.site.register(Author)
admin.site.register(BookCard)
admin.site.register(Genre)
admin.site.register(Favorites)
