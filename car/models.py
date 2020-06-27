import uuid
from django.db import models
from django.utils.translation import gettext as _

class Car(models.Model):

    TTR_M = 1
    TTR_A = 2
    TTR_V = 3

    TTR_CHOICES = [
        (TTR_M, "Механика"),
        (TTR_A, "Автомат"),
        (TTR_V, "Робот"),
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                           verbose_name=_("Уникальный ключ"))
    manufacturer = models.CharField(max_length=256, verbose_name=_("Производитель"))
    model = models.CharField(max_length=256, verbose_name=_("Модель авто"))
    year_of_manufacture = models.SmallIntegerField(verbose_name=_("Год выпуска"))
    transmission = models.IntegerField("Коробка передач", choices=TTR_CHOICES)
    color = models.CharField(max_length=256, verbose_name=_("Цвет"))
    name = models.CharField(max_length=999, verbose_name=_("Наименование"))

    def __str__(self):
        return f"""{self.name}"""

    def save(self, *args, **kwargs):
        self.name = f"""{self.manufacturer} {self.model} {self.year_of_manufacture} {self.get_transmission_display()} {self.color}"""
        super(Car, self).save(*args, **kwargs)
