from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(
        "Имя", max_length=settings.SHORT_FIELD_LENGTH
    )
    last_name = models.CharField(
        "Фамилия", max_length=settings.SHORT_FIELD_LENGTH
    )
    patronymic = models.CharField(
        "Отчество",
        max_length=settings.SHORT_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    bio = models.TextField(
        "Биография",
        max_length=settings.LONG_FIELD_LENGTH,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=settings.SHORT_FIELD_LENGTH)
    slug = models.SlugField(
        "Slug", max_length=settings.SHORT_FIELD_LENGTH, unique=True
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):
    pub_date = models.DateTimeField(
        "Дата и время добавления", auto_now_add=True, editable=False
    )
    last_update = models.DateTimeField(
        "Дата последнего обновления", auto_now=True, editable=False
    )
    title = models.CharField(
        "Название", max_length=settings.MEDIUM_FIELD_LENGTH
    )
    description = models.TextField(
        "Описание",
        max_length=settings.LONG_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    cover = models.ImageField(
        "Обложка", upload_to="books/img/", blank=True, null=True
    )
    authors = models.ManyToManyField(
        "Author", verbose_name="Авторы", related_name="books", blank=True
    )
    genres = models.ManyToManyField(
        "Genre", verbose_name="Жанры", related_name="books", blank=True
    )
    isbn = models.CharField(
        "Уникальный номер (ISBN)",
        max_length=settings.SHORT_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    year = models.PositiveSmallIntegerField("Год", blank=True, null=True)
    num_of_pages = models.PositiveSmallIntegerField(
        "Число страниц", blank=True, null=True
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class BookCard(models.Model):
    BOOK_CONDITIONS = (
        ("NEW", "Новое"),
        ("EXCELLENT", "Отличное"),
        ("GOOD", "Хорошее"),
        ("AVERAGE", "Среднее"),
    )

    pub_date = models.DateTimeField(
        "Дата и время публикации", auto_now_add=True, editable=False
    )
    last_update = models.DateTimeField(
        "Дата последнего обновления", auto_now=True, editable=False
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="book_cards",
        verbose_name="Владелец",
    )
    title = models.CharField(
        "Название", max_length=settings.MEDIUM_FIELD_LENGTH
    )
    description = models.TextField(
        "Описание",
        max_length=settings.LONG_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        "Фотография", upload_to="book_card/img/", blank=True, null=True
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        related_name="book_cards",
        verbose_name="Книга",
        blank=True,
        null=True,
    )
    condition = models.CharField(
        "Состояние",
        max_length=settings.SHORT_FIELD_LENGTH,
        choices=BOOK_CONDITIONS,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="favorites",
    )
    book_card = models.ForeignKey(
        BookCard,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        related_name="favorites",
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

    def __str__(self):
        return f"{self.user.email} <--> {self.book_card.title}"


class BookApplication(models.Model):
    book_card = models.ForeignKey(
        BookCard,
        on_delete=models.CASCADE,
        verbose_name="Объявление",
        related_name="applications",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        related_name="applications",
        blank=True,
        null=True
    )
    name = models.CharField(
        "Имя", max_length=settings.MEDIUM_FIELD_LENGTH
    )
    phone = models.CharField(
        "Телефон", max_length=settings.SHORT_FIELD_LENGTH
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.book_card.title} --> {self.user.email}"
