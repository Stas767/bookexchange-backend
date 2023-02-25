from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

# Удалить в следующей версии api
EXCHANGE_CHOICES = (
    ('PERSONAL', 'Личная встреча'),
    ('PICKUP_POINT', 'Доставка в отделение или пункт выдачи'),
    ('COURIER', 'Курьерская доставка'),
)
# ------------------------------


class CustomUser(AbstractUser):

    email = models.EmailField(
        'Email', max_length=settings.MEDIUM_FIELD_LENGTH, unique=True
    )
    phone = models.CharField(
        'Телефон', max_length=settings.SHORT_FIELD_LENGTH, blank=True,
        null=True
    )
    city = models.CharField(
        'Город', max_length=settings.SHORT_FIELD_LENGTH, blank=True, null=True
    )

    # Удалить в следующей версии api
    subway = models.CharField(
        'Метро',
        max_length=50,
        blank=True,
        null=True
    )
    exchange = models.CharField(
        'Вариант обмена',
        max_length=50,
        choices=EXCHANGE_CHOICES,
    )
    # ------------------------------

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
