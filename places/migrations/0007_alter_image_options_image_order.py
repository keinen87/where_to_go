# Generated by Django 4.0.5 on 2022-06-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
