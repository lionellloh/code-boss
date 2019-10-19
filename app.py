from flask import render_template, url_for, redirect, Flask, render_template, request, session, jsonify
import json
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from lib import find_places, current_location, string_find_place
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

login_manager = LoginManager()
app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy()
migrate = Migrate(app, db)
# app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root@localhost/codebossdb'
from models import *

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = os.getenv("GOOGLEMAPS_KEY")

# Initialize the extension
GoogleMaps(app)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
    
@app.route("/restaurant", methods=['POST','GET'])
def restaurant_list_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            # TODO: Add 0s
            latitude = request.form['field1']+"00000"
            longitude = request.form['field2']+"000000"

            try:
                radius = int(float(request.form['field3']))

            except:
                radius = 1000
            # places = [{'address': 'Rd, Singapore',
            # 'name': 'Kamat Indian Food Stall',
            # 'open_now': False,
            # 'num_ratings': 13,
            # 'rating': 3.3}]
            # places = find_places(latitude, longitude, radius)

            if not radius:
                radius = 1000

            if not latitude or not longitude:
                places = find_places()

            else:
                places = find_places(latitude, longitude, radius)
            print(places)
            return render_template("restaurantList.html", results=places)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("restaurantList.html", results=[])


# @app.route("/current_loc", methods=['POST', 'GET'])
# def current_location():
#
#     latlng = current_location()
#     return latlng


@app.route("/search", methods=['POST','GET'])
def search_text():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            search_text = request.form['field1']
            markers = string_query(search_text)
            print("MARKERS", markers)
            first = [(markers[0])]
            second = markers[1:]
            print("SECOND", second)
            print(len(second))
            markers = [
                {'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': first[0][0],
                'lng': first[0][1]}]

            markers.extend([
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat':point[0],
                    'lng':point[1]
                }
                for point in second
            ])

            print(markers)
            sndmap = Map(
                identifier="sndmap",
                lat=first[0][0],
                lng=first[0][1],
                markers=markers
            )
            return render_template('map.html', sndmap=sndmap)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("searchtext.html")


@app.route("/", methods=['POST','GET'])
def restaurants_near_me():
    latlng = tuple(current_location())

    print(latlng)
    second = find_places(latlng[0], latlng[1])
    second = [(e["lat"], e["lng"]) for e in second]
    print("SECOND", second)
    latlng = [latlng]
    latlng.extend(second)
    markers = latlng

    print("LATLNG", latlng)

    markers = [
        {'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
         'lat': latlng[0][0],
         'lng': latlng[0][1]}]

    markers.extend([
        {
            'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'lat': point[0],
            'lng': point[1]
        }
        for point in second
    ])

    print(markers)
    sndmap = Map(
        identifier="sndmap",
        lat=latlng[0][0],
        lng=latlng[0][1],
        markers=markers
    )
    return render_template('map.html', sndmap=sndmap)

    return jsonify(nearby)


# @app.route("/query", methods=['POST', 'GET'])
def string_query(query = None):
    if not query:
        query = "Raffles Place, Bank of Singapore"
    places= []
    # print(string_find_place(query))
    # try:
    lat, lng = string_find_place(query)
    output = [(lat, lng)]
    found_places = find_places(lat=str(lat), lng=str(lng))
    # print(found_places)
    places = [(o["lat"], o["lng"]) for o in found_places]
    # print("output", output)
    # print("places", places)

    return places





if __name__ == '__main__':
    app.run()
