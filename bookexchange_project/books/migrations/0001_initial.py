# Generated by Django 2.2.16 on 2023-01-26 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(help_text='Введите название произведения', max_length=255, verbose_name='Название книги')),
                ('author_name', models.CharField(help_text='Введите имя автора', max_length=255, verbose_name='Автор книги')),
                ('genre', models.CharField(blank=True, help_text='Какой жанр у книги?', max_length=255, null=True, verbose_name='Жанр')),
                ('book_description', models.TextField(help_text='О чем эта книга?', max_length=1000, verbose_name='Описание книги')),
                ('book_image', models.ImageField(blank=True, help_text='Приложите фотографию книги', null=True, upload_to='books/')),
                ('isbn', models.CharField(help_text='ISBN - это уникальный индентификатор книги. Он може быть указан на первой странице или с обратной стороны книги.', max_length=100, verbose_name='International Standard Book Number')),
                ('condition', models.CharField(choices=[('Новый/(ая)', 'Новый/(ая)'), ('Как новый/(ая)', 'Как новый/(ая)'), ('Очень хорошее', 'Очень хорошее'), ('Достойное', 'Достойное'), ('Приемлемое', 'Приемлемое'), ('Практически приемлемое', 'Практически приемлемое')], default='Укажите состояние книги', help_text='Выберите из списка состояние данного экземпляра.', max_length=120, verbose_name='Состояние книги')),
                ('year', models.IntegerField(default=1999, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs', to='books.BookCard')),
            ],
        ),
    ]
