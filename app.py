from flask import render_template, url_for, redirect, Flask, render_template, request, session, jsonify
import json
from lib import find_places, current_location, string_find_place
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy()
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root@localhost/codebossdb'
from models import *

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/restaurant", methods=['POST','GET'])
def restaurant_list_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            latitude = request.form['field1']
            longitude = request.form['field2']
            radius = int(float(request.form['field3']))
            search_criteria = [latitude, longitude, radius]
            # book_list = get_book([latitude, longitude, radius])

            places = find_places(latitude, longitude, radius)
            print(places)

            return render_template("restaurantList.html", results=places)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("restaurantList.html", results=[])


@app.route("/current_loc", methods=['POST', 'GET'])
def current_location_api():

    latlng = current_location()
    return latlng


@app.route("/query", methods=['POST', 'GET'])
def string_query():
    query = "Raffles Place, Bank of Singapore"
    places= []
    print(string_find_place(query))
    # try:
    lat, lng = string_find_place(query)
    output = [[lat, lng]]
    found_places = find_places(lat=str(lat), lng=str(lng))
    print(found_places)
    places = [[o["lat"], o["lng"]] for o in found_places]
    print("output", output)
    print("places", places)


    return jsonify(places)





if __name__ == '__main__':
    app.run()
