# Generated by Django 3.0.7 on 2020-06-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.IntegerField(choices=[(1, 'Механика'), (2, 'Автомат'), (3, 'Робот')], verbose_name='Коробка передач'),
        ),
    ]