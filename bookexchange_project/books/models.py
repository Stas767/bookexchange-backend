from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from books.constants import BOOK_CONDITIONS, DEAL_TYPES

User = get_user_model()


class Advert(models.Model):
    # объявление
    pub_date = models.DateTimeField(
        'Дата и время создания', auto_now_add=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Владелец',
        related_name='adverts',
    )
    title = models.CharField(
        'Название', max_length=settings.SHORT_FIELD_LENGTH
    )
    description = models.TextField(
        'Описание', max_length=settings.LONG_FIELD_LENGTH, blank=True,
        null=True
    )

    # книга
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, verbose_name='Книга',
        related_name='adverts'
    )
    book_image = models.ImageField(
        'Фотография', upload_to='adverts/img/', blank=True, null=True
    )
    book_condition = models.CharField(
        'Состояние', max_length=settings.SHORT_FIELD_LENGTH,
        choices=BOOK_CONDITIONS
    )

    # сделка
    deal_type = models.CharField(
        'Тип сделки', max_length=settings.SHORT_FIELD_LENGTH,
        choices=DEAL_TYPES
    )
    deal_terms = models.TextField('Условия сделки', max_length=600)

    # контактная информация
    contact_phone = models.CharField(
        'Телефон', max_length=settings.SHORT_FIELD_LENGTH
    )
    contact_email = models.EmailField('Email', blank=True, null=True)
    contact_telegram = models.CharField(
        'Телеграм', max_length=settings.SHORT_FIELD_LENGTH, blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.id


class Book(models.Model):

    pub_date = models.DateTimeField(
        'Дата и время добавления', auto_now_add=True
    )
    title = models.CharField(
        'Название', max_length=settings.SHORT_FIELD_LENGTH
    )
    description = models.TextField(
        'Описание', max_length=settings.LONG_FIELD_LENGTH, blank=True,
        null=True
    )
    cover = models.ImageField(
        'Обложка', upload_to='books/img/', blank=True, null=True
    )
    authors = models.ManyToManyField(
        'Author', verbose_name='Авторы', related_name='books'
    )
    genres = models.ManyToManyField(
        'Genre', verbose_name='Жанры', related_name='books'
    )
    isbn = models.CharField(
        'Уникальный номер (ISBN)', max_length=settings.SHORT_FIELD_LENGTH,
        blank=True, null=True
    )
    year = models.PositiveSmallIntegerField('Год', blank=True, null=True)
    pages = models.PositiveSmallIntegerField(
        'Число страниц', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.id


class Author(models.Model):

    first_name = models.CharField(
        'Имя', max_length=settings.SHORT_FIELD_LENGTH
    )
    last_name = models.CharField(
        'Фамилия', max_length=settings.SHORT_FIELD_LENGTH
    )
    surname = models.CharField(
        'Отчество', max_length=settings.SHORT_FIELD_LENGTH
    )
    bio = models.TextField(
        'Биография', max_length=settings.LONG_FIELD_LENGTH
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.id


class Genre(models.Model):

    name = models.CharField('Жанр', max_length=settings.SHORT_FIELD_LENGTH)
    slug = models.SlugField(
        'Slug', max_length=settings.SHORT_FIELD_LENGTH, unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.id


class Favorites(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь',
        related_name='favorites'
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, verbose_name='Книга',
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return self.id
