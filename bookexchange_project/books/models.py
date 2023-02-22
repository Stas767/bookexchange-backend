from django.db import models
from django.contrib.auth import get_user_model

from books import constants


User = get_user_model()


class BookCard(models.Model):
    '''Модель книги.'''

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Владелец книги'
    )
    title = models.CharField(
        'Название книги',
        max_length=255,
        help_text='Введите название произведения'
    )
    # Это поле переписать на FK таблицы с автором. Таблицу сделать. 
    author = models.CharField(
        'Автор книги',
        max_length=255,
        help_text='Введите имя автора'
    )
    # Аналогично
    genre = models.CharField(
        'Жанр',
        max_length=255,
        blank=True,
        null=True,
        help_text='Какой жанр у книги?'
    )
    description = models.TextField(
        'Описание книги',
        max_length=1000,
        blank=True,
        null=True,
        help_text='О чем эта книга?'
    )
    # Тут нужно указать актуальный путь для медиа.
    image = models.ImageField(
        'Фотография книги',
        upload_to='backend_media/book_cover/',
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
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True
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
        User,
        default=None,
        on_delete=models.CASCADE,
        related_name='favs'
    )
