from django.db import models

from books import constants
from users.models import CustomUser


class BookCard(models.Model):
    '''Модель книги.'''

    publisher = models.ForeignKey(
        CustomUser,
        default=None,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Владелец книги'
    )
    book_title = models.CharField(
        'Название книги',
        max_length=255,
        help_text='Введите название произведения'
    )
    author_name = models.CharField(
        'Автор книги',
        max_length=255,
        help_text='Введите имя автора'
    )
    genre = models.CharField(
        'Жанр',
        max_length=255,
        blank=True,
        null=True,
        help_text='Какой жанр у книги?'
    )
    book_description = models.TextField(
        'Описание книги',
        max_length=1000,
        blank=True,
        null=True,
        help_text='О чем эта книга?'
    )
    # Тут нужно указать актуальный путь для медиа.
    book_image = models.ImageField(
        'Фотография книги',
        upload_to='books/',
        null=True,
        blank=True,
        help_text='Приложите фотографию книги'
    )
    isbn = models.CharField(
        'International Standard Book Number',
        max_length=100,
        null=True,
        blank=True,
        help_text='ISBN - это уникальный индентификатор книги. Он може быть указан на первой странице или с обратной стороны книги.',
    )
    condition = models.CharField(
        'Состояние книги',
        null=True,
        blank=True,
        # Как на твой взгляд, приемлимо так делать choise?
        choices=constants.CONDITIONS_RUS,
        help_text='Выберите из списка состояние данного экземпляра.'
    )
    year = models.IntegerField(
        'Год издания',
        null=True,
        blank=True,
        default=1999
    )

    def __str__(self):
        return self.book_title


class Favorites(models.Model):

    book_card = models.ForeignKey(
        BookCard,
        on_delete=models.CASCADE,
        related_name='favs'
    )
    user = models.ForeignKey(
        CustomUser,
        default=None,
        on_delete=models.CASCADE,
        related_name='favs'
    )
