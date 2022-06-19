from turtle import width
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.TabularInline):
    def headshot_image(self, image):
        html = format_html(
            """<img src="{}" width="{}" height={} />""",
            image.image.url,
            200,
            200
        )

        return html

    readonly_fields = ["headshot_image"]
    model = Image
    fields = (("image",  "headshot_image"))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ["title", "place_id"]
