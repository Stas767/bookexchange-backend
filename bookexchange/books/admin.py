from django.contrib import admin

from books.models import (
    Author,
    Book,
    BookApplication,
    BookCard,
    Favorites,
    Genre,
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookApplication)
admin.site.register(BookCard)
admin.site.register(Favorites)
admin.site.register(Genre)
