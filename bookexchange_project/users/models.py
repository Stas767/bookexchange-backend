from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
