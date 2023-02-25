from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from books.constants import BOOK_CONDITIONS, DEAL_TYPES

User = get_user_model()


# Удалить в следующей версии api
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
        'Author',
        verbose_name='Автор книги',
        related_name='book_cards'
    )
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        related_name='book_cards'
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
        upload_to='book_cover/',
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
        choices=BOOK_CONDITIONS,
        help_text='Выберите из списка состояние данного экземпляра.'
    )
    year = models.IntegerField(
        'Год издания',
        null=True,
        blank=True
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Карточка книги'
        verbose_name_plural = 'Карточки книг'

    def __str__(self):
        return self.title[:40]
# ------------------------------


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
        return self.title[:40]


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
        return self.title[:40]


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
        return f'{self.last_name} {self.first_name}'


class Genre(models.Model):

    name = models.CharField('Жанр', max_length=settings.SHORT_FIELD_LENGTH)
    slug = models.SlugField(
        'Slug', max_length=settings.SHORT_FIELD_LENGTH, unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Favorites(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь',
        related_name='favorites'
    )
    # В новой версии api заменить связь на Объявление
    book_card = models.ForeignKey(
        BookCard, on_delete=models.CASCADE, verbose_name='Книга',
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.user_id} <--> {self.advert_id}'
