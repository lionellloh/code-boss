from flask import render_template, url_for, redirect, Flask, render_template, request, session
import json
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDagEGHGxQzxQHJ0OlD3SGyrBlOJUhAqrk"

# Initialize the extension
GoogleMaps(app)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route("/restaurant", methods=['POST','GET'])
def book_list_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            latitude = request.form['field1']
            longitude = request.form['field2']
            radius = request.form['field3']
            search_criteria = [latitude, longitude, radius]
            places = [{'address': 'Rd, Singapore', 
            'name': 'Kamat Indian Food Stall', 
            'open_now': False, 
            'num_ratings': 13, 
            'rating': 3.3}]
            # places = find_places(latitude, longitude, radius)
            print(places)
            return render_template("restaurantList.html", results=places)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("restaurantList.html", results=[])

@app.route("/searchtext", methods=['POST','GET'])
def search_text():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            search_text = request.form['field1']
            # markers = find_markers(search_text)
            list_returned = []
            markers_returned = [(37.4419,-122.1419),
            (37.4300,-122.1400),(37.4500,-122.1500)]
            first = markers_returned[:1]
            second = markers_returned[1:]
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
            sndmap = Map(
                identifier="sndmap",
                lat=first[0][0],
                lng=second[0][1],
                markers=markers
            )
            return render_template('map.html', sndmap=sndmap)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("searchtext.html", results=[])

if __name__ == '__main__':
    app.run()
