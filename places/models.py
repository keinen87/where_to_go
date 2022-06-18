from msilib.schema import Class
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",)
    description_long = models.TextField(verbose_name="Длинное описание",)
    description_short = models.TextField(
        verbose_name="Короткое описание",
        null=True
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    place_id = models.CharField(max_length=200, verbose_name="id")

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        related_name="images",
        verbose_name="Место",
    )

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="images",
    )

    def __str__(self) -> str:
        return f"{self.place.title}"
