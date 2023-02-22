from django.contrib import admin

from .models import BookCard, Faforites, Authors, Genres


admin.site.register(BookCard)
admin.site.register(Faforites)
admin.site.register(Authors)
admin.site.register(Genres)
