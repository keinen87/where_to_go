import json
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place


def get_json_local():
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    folder_path = f"{os.path.join(settings.BASE_DIR, 'static')}/places/"
    fiels = os.listdir(folder_path)

    for file in fiels:
        file_path = f"{folder_path}{file}"
        with open(file_path, "r", encoding="utf-8") as file:
            file = json.load(file)

            geo_json["features"].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [file["coordinates"]["lng"], file["coordinates"]["lat"]]
                },
                "properties": {
                    "title": file["title"],
                    "placeId": file["title"],
                    "detailsUrl": f"{settings.STATIC_URL}places/{file['title']}.json"
                }
            })

    return geo_json


def get_json_db(places):
    for place in places:
        json_path = f"{os.path.join(settings.BASE_DIR, 'static')}/places/{place.title}.json"

        if not os.path.exists(json_path):
            create_json(place, json_path)

    return


def create_json(place, json_path):
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


def show_maps(request):
    places = Place.objects.all()
    get_json_db(places)
    geo_json_local = get_json_local()

    data = {"GeoJSON": geo_json_local}

    return render(request, "index.html", context=data)
