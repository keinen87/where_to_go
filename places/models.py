from msilib.schema import Class
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",)
    description_long = models.TextField(verbose_name="Длинное описание",)
    description_short = models.TextField(verbose_name="Короткое описание",)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
