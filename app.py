from flask import render_template, url_for, redirect, Flask, render_template, request, session
import json
from lib import find_places

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/restaurant", methods=['POST','GET'])
def book_list_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            latitude = request.form['field1']
            longitude = request.form['field2']
<<<<<<< HEAD
            radius = request.form['field3']
            search_text = request.form['field4']
            search_criteria = [latitude, longitude, radius, search_text]
=======
            radius = int(float(request.form['field3']))
            search_criteria = [latitude, longitude, radius]
>>>>>>> 61f8939e62071b3a7e3dcc84698a5471cc2b9160
            # book_list = get_book([latitude, longitude, radius])

            places = find_places(latitude, longitude, radius)
            print(places)

            return render_template("restaurantList.html", results=places)
    else:
        # book_list = [{"address":"street1","name":"best rest"}]
        return render_template("restaurantList.html", results=[])

if __name__ == '__main__':
    app.run()
