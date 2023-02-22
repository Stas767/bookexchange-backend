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
    author = models.ManyToManyField(
        'Authors',
        verbose_name='Автор книги',
    )
    genre = models.ManyToManyField(
        'Genres',
        verbose_name='Жанр'
    )
    description = models.TextField(
        'Описание книги',
        max_length=1000,
        blank=True,
        null=True,
        help_text='О чем эта книга?'
    )
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
        max_length=50,
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
    faforites = models.ManyToManyField(
        'Faforites',
        verbose_name='Избранное'
    )

    class Meta:
        verbose_name = 'Карточка книги'
        verbose_name_plural = 'Карточки книг'

    def __str__(self):
        return self.title[:40]


class Faforites(models.Model):
    '''Избраное.'''

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

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class Authors(models.Model):
    '''Авторы книг.'''

    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    surname = models.CharField('Отчество', max_length=50)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genres(models.Model):
    '''Жанры книг.'''

    name = models.CharField('Жанр', max_length=50)
    slug = models.SlugField('Slug', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
