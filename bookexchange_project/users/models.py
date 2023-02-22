from django.contrib.auth.models import AbstractUser
from django.db import models

# Эти choise нужно перенести в другой файл. После пула актуальной структуры проекта исправлю.
ADMIN = 'admin'
USER = 'user'

ROLE = (
    (USER, 'Пользователь'),
    (ADMIN, 'Администратор')
)

SUBWAY = 'subway'
MAIL = 'mail'
MEETING = 'meeting'

UserExchange = (
    ('SUBWAY', 'Метро'),
    ('MAIL', 'Почта'),
    ('MEETING', 'При встрече')
)


class CustomUser(AbstractUser):
    '''Кастомная модель пользователя'''

    username = models.CharField(
        'Имя',
        max_length=50
    )
    phone = models.CharField(
        'Телефон',
        blank=True,
        null=True
    )
    # С этим полем нужно решить, как мы отдаем города.
    # Либо вводим перечень городов по дефолту и пользователь выбирет сам,
    # либо делаем поле уникальным и даем возможность наполнять БД данными от пользователя.
    city = models.CharField(
        'Город',
        max_length=35,
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
        max_length=20,
        default=SUBWAY,
        choices=UserExchange,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
        max_length=254
    )
    # Это поле добавил от себя, так в любом случае нужен админ сайта.
    role = models.CharField(
        'Роль пользователя',
        max_length=10,
        choices=ROLE,
        default=USER,
        help_text=(
            'Администратор или пользователь. По умолчанию пользователь.'
        ),
        blank=True
    )
    password = models.CharField(
        'Пароль',
        max_length=150
    )

    def __str__(self) -> str:
        return f'{self.username}'

# Этот constraints тоже под вопросом. Вроде все логично, не я его писал. Требует коммента.
    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_username_email_pair'
            )
        ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):

        return bool(self.role == ADMIN)
