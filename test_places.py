import requests
import json
import random
from googleplaces import GooglePlaces, types, lang
APIKEY = "AIzaSyBFx8hqftDOlrSWRTiOSowjwfeS1OQtBpw"
from collections import defaultdict

google_places = GooglePlaces(APIKEY)

def find_places(lat = "1.284340", lng = "103.852320", radius=200, pagetoken=None):
    lat, lng
    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': lng},
        radius=radius,
        types=[types.TYPE_RESTAURANT])

    output = []

    api_results = dict(query_result.raw_response)["results"]
    for res in api_results:
        res = defaultdict(int, res)
        output.append(
            dict(address=res["vicinity"],
             name=res["name"],
             open_now=random.random() > 0.2,
             num_ratings=res["user_ratings_total"],
             rating=res["rating"]
             )
        )


    return output

if __name__ == "__main__":
    print(find_places())