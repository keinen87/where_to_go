import json
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place


def show_maps(request):
    places = Place.objects.all()
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        json_path = f"{os.path.join(settings.BASE_DIR, 'static')}/places/{place.title}.json"

        with open(json_path, "w", encoding="utf8") as file:
            deatils_url = {
                "title": place.title,
                "imgs": [image.image.url for image in place.images.all()],
                "description_short": place.description_short,
                "description_long": place.description_long,
                "coordinates": {
                    "lat": place.latitude,
                    "lng": place.longitude
                }
            }

            json.dump(deatils_url, file, ensure_ascii=False, indent=4)

        geo_json["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": f"{settings.STATIC_URL}places/{place.title}.json"
            }
        })

    data = {"GeoJSON": geo_json}

    return render(request, 'index.html', context=data)
