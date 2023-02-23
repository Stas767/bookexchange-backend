from django.contrib.auth.models import AbstractUser
from django.db import models


ExchangeChoices = (
    ('SUBWAY', 'Метро'),
    ('MAIL', 'Почта'),
    ('MEETING', 'При встрече')
)


class CustomUser(AbstractUser):
    '''Кастомная модель пользователя'''

    phone = models.CharField(
        'Телефон',
        max_length=50,
        blank=True,
        null=True
    )
    # С этим полем нужно решить, как мы отдаем города.
    # Либо вводим перечень городов по дефолту и пользователь выбирет сам,
    # либо делаем поле уникальным и даем возможность наполнять БД данными от пользователя.
    city = models.CharField(
        'Город',
        max_length=50,
        blank=True,
        null=True
    )
    # Аналогично
    subway = models.CharField(
        'Метро',
        max_length=50,
        blank=True,
        null=True
    )
    exchange = models.CharField(
        'Вариант обмена',
        max_length=50,
        choices=ExchangeChoices,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True
    )

    def __str__(self) -> str:
        return f'{self.username}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
