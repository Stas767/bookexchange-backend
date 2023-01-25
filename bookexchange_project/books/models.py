from django.contrib.auth import get_user_model
from django.db import models

from . import constants

# Сделать миграции
# Написать условие для определения языка (возможно)

User = get_user_model()


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    last_name = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    father_name = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    # birth_date = models.DateTimeField(
    #     'Date of birth',
    #     auto_now_add=False,
    # )

    def __str__(self):
        if self.father_name == '':
            return f'{self.first_name[0]}.{self.last_name}'
        else:
            return f'{self.first_name[0]}.{self.father_name[0]}.{self.last_name}'
        # Сделать так, чтобы возвращал слитно инициалы


class PubAuthor(models.Model):
    username = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    email = models.EmailField(max_length=80)
    first_name = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    last_name = models.CharField(max_length=constants.NAME_DEFAULT_LENGTH)
    phone = models.IntegerField(
        verbose_name='Phone number',
        help_text='+7-XXX-XXX-XX-XX'
    )
    birth_date = models.DateTimeField(
        'Date of birth',
        auto_now_add=False,
    )

    def __str__(self):
        return self.username


class Genre(models.Model):
    genre_title = models.CharField(
        max_length=120,
        choices=constants.GENRES_RUS
        )
    slug = models.SlugField()
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание жанра',
        default='Отсутствует..'
    )

    def __str__(self):
        return self.genre_title


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название книги'
    )
    book_author = models.ForeignKey(
        BookAuthor,
        on_delete=models.CASCADE,
        related_name='books',
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Кратко о книге',
    )
    book_image = models.ImageField(
        upload_to='books/',
        null=True,
        blank=True      # Доработать шаблон с картинкой книги.
    )
    isbn = models.CharField(
        max_length=100,
        verbose_name='International Standard Book Number',
        help_text='ISBN это уникальный индентификатор книги.',
    )
    condition = models.CharField(
        max_length=120,
        choices=constants.CONDITIONS_RUS,
        verbose_name='Состояние книги',
        # help_text='Выберите из списка состояние данного экземпляра.'
        default='Укажите состояние книги',
    )
    pub_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
    )
    creation_date = models.DateField()
    pub_date = models.DateTimeField(
        'Дата публикации книги на платформе.',
        auto_now_add=True,
    )
    gentre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='books',
        blank=True,
        null=True
    )
    downloadable = models.BooleanField(default=False)

    # Обратить внимание, может надо выбрать другой тип поля для lang_id.
    # ALL2Cart использует передачу индекса туда из... Мб модели
    # lang_id = models.CharField(
    #     default=' ',
    #     max_length=50,
    #     choices=constants.LANG,
    # )

    # pages = models.IntegerField(
    #     blank=True,
    #     null=True,
    # )

    def __str__(self):
        return self.title
