from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

BOOK_CONDITIONS = (
    ('NEW', 'Новое'),
    ('EXCELLENT', 'Отличное'),
    ('GOOD', 'Хорошее'),
    ('AVERAGE', 'Среднее'),
)


class BookCard(models.Model):

    pub_date = models.DateTimeField(
        'Дата и время публикации', auto_now_add=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_card',
        verbose_name='Владелец'
    )
    title = models.CharField(
        'Название', max_length=settings.MEDIUM_FIELD_LENGTH
    )
    description = models.TextField(
        'Описание', max_length=settings.LONG_FIELD_LENGTH, blank=True,
        null=True,
    )
    image = models.ImageField(
        'Фотографии', upload_to='book_card/img/', blank=True, null=True
    )
    author = models.ManyToManyField(
        'Author', verbose_name='Автор', related_name='book_card'
    )
    genre = models.ManyToManyField(
        'Genre', verbose_name='Жанр', related_name='book_card'
    )
    isbn = models.CharField(
        'ISBN', max_length=settings.SHORT_FIELD_LENGTH, blank=True, null=True        
    )
    condition = models.CharField(
        'Состояние', max_length=settings.SHORT_FIELD_LENGTH, blank=True,
        null=True, choices=BOOK_CONDITIONS
    )
    year = models.PositiveSmallIntegerField(
        'Год издания', blank=True, null=True
    )
    

    class Meta:
        verbose_name = 'Карточка книги'
        verbose_name_plural = 'Карточки книг'

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
    book_card = models.ForeignKey(
        BookCard, on_delete=models.CASCADE, verbose_name='Книга',
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.user_id} <--> {self.advert_id}'
