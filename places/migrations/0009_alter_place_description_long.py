# Generated by Django 4.0.5 on 2022-06-19 21:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_options_place_order_alter_image_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Длинное описание'),
        ),
    ]
