from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    EXCHANGE_CHOICES = (
        ("PERSONAL", "Личная встреча"),
        ("PICKUP_POINT", "Доставка в отделение или пункт выдачи"),
        ("COURIER", "Курьерская доставка"),
    )

    first_name = models.CharField(
        "Имя", max_length=settings.SHORT_FIELD_LENGTH, blank=True, null=True
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=settings.SHORT_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        "Email", max_length=settings.SHORT_FIELD_LENGTH, unique=True
    )
    phone = models.CharField(
        "Телефон",
        max_length=settings.SHORT_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    city = models.CharField(
        "Город", max_length=settings.SHORT_FIELD_LENGTH, blank=True, null=True
    )
    subway = models.CharField(
        "Метро", max_length=settings.SHORT_FIELD_LENGTH, blank=True, null=True
    )
    exchange = models.CharField(
        "Вариант обмена",
        max_length=settings.SHORT_FIELD_LENGTH,
        choices=EXCHANGE_CHOICES,
        blank=True,
        null=True,
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        "Дата регистрации", auto_now_add=True, editable=False
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return "{} {} | {}".format(self.last_name, self.first_name, self.email)
