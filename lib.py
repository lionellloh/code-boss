import requests
import json
import random
import geocoder
from googleplaces import GooglePlaces, types, lang
import googlemaps
import geocoder
from pprint import pprint
from datetime import datetime

APIKEY = "AIzaSyBFx8hqftDOlrSWRTiOSowjwfeS1OQtBpw"
from collections import defaultdict

google_places = GooglePlaces(APIKEY)
gmaps = googlemaps.Client(key= "AIzaSyDU8rHEpvfpXuTHUlEL86X3CCUmgzzE8fU")

def find_places(lat = "1.284340", lng = "103.852320", radius=500):
    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': lng},
        radius=radius,
        types=[types.TYPE_RESTAURANT])

    output = []

    api_results = dict(query_result.raw_response)["results"]
    # pprint(api_results)
    for res in api_results:
        res = defaultdict(int, res)
        output.append(
            dict(
             lat = str(res["geometry"]["location"]["lat"]),
             lng = str(res["geometry"]["location"]["lng"]),
             address=res["vicinity"],
             name=res["name"],
             open_now=random.random() > 0.2,
             num_ratings=res["user_ratings_total"],
             rating=str(round(res["rating"],2))
             )
        )

    return output


def string_find_place(query ="Bank of Singapore, Raffles Place"):
    geocode_result = gmaps.geocode(query)

    # pprint(geocode_result)
    loc = geocode_result[0]["geometry"]["location"]
    latlng = (loc["lat"], loc["lng"])

    return latlng

def current_location():

    g = geocoder.ip('me')
    return (g.latlng)



if __name__ == "__main__":
    results = find_places()


    print(results)
    # print(current_location())
    # # print(find_places())