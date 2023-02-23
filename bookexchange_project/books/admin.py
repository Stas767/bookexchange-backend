from django.contrib import admin

from .models import BookCard, Faforites, Author, Genre


admin.site.register(BookCard)
admin.site.register(Faforites)
admin.site.register(Author)
admin.site.register(Genre)
