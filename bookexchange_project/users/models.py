'''Переопределяем и расширяем стандартную модель пользователя.'''

from django.contrib.auth.models import AbstractUser
from django.db import models


UserExchange = (
    ('SUBWAY', 'Метро'),
    ('MAIL', 'Почта'),
    ('MEETING', 'При встрече')
)


class User(AbstractUser):

    # class UserExchange(models.TextChoices):
    #     SUBWAY = 'Метро', 'В метро'
    #     MAIL = 'Почта', 'По почте'
    #     MEETING = 'При встрече', 'При встрече'

    phone = models.IntegerField(
        # max_length=10,
        default=9999999999,
        blank=True,
        help_text='Введите номер телефона.',
        verbose_name='Телефон'
    )
    city = models.CharField(
        max_length=35,
        blank=True,
        null=True
    )
    exchange = models.CharField(
        'Вариант обмена',
        max_length=20,
        default=UserExchange[1],
        choices=UserExchange,
    )

    def __str__(self) -> str:
        return f'{self.username}'

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_username_email_pair'
            )
        ]
