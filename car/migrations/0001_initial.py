# Generated by Django 3.0.7 on 2020-06-27 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Уникальный ключ')),
                ('manufacturer', models.CharField(max_length=256, verbose_name='Производитель')),
                ('model', models.CharField(max_length=256, verbose_name='Модель авто')),
                ('year_of_manufacture', models.SmallIntegerField(verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[(1, 'Механика'), (2, 'Автомат'), (3, 'Робот')], max_length=10)),
                ('color', models.CharField(max_length=256, verbose_name='Цвет')),
                ('name', models.CharField(max_length=999, verbose_name='Наименование')),
            ],
        ),
    ]
