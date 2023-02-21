from django.db import models

from books import constants
from users.models import User

class BookCard(models.Model):

    publisher = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book_title = models.CharField(
        max_length=255,
        verbose_name='Название книги',
        help_text='Введите название произведения'
    )
    author_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Автор книги',
        help_text='Введите имя автора'
    )
    genre = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Жанр',
        help_text='Какой жанр у книги?'
    )
    book_description = models.TextField(
        max_length=1000,
        verbose_name='Описание книги',
        help_text='О чем эта книга?'
    )
    book_image = models.ImageField(
        upload_to='books/',
        null=True,
        blank=True,
        help_text='Приложите фотографию книги'
    )
    isbn = models.CharField(
        max_length=100,
        verbose_name='International Standard Book Number',
        help_text='ISBN - это уникальный индентификатор книги. Он може быть указан на первой странице или с обратной стороны книги.',
    )
    condition = models.CharField(
        max_length=120,
        choices=constants.CONDITIONS_RUS,
        verbose_name='Состояние книги',
        help_text='Выберите из списка состояние данного экземпляра.',
        default='Укажите состояние книги',
    )
    year = models.IntegerField(default=1999)

    def __str__(self):
        return self.book_title


class Favorites(models.Model):

    book_card = models.ForeignKey(
        BookCard,
        on_delete=models.CASCADE,
        related_name='favs'
    )
    user = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
        related_name='favs'
    )
