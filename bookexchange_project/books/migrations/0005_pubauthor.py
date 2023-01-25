# Generated by Django 2.2.16 on 2022-12-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20221226_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', models.IntegerField(help_text='+7-XXX-XXX-XX-XX', verbose_name='Phone number')),
                ('birth_date', models.DateTimeField(verbose_name='Date of birth')),
            ],
        ),
    ]