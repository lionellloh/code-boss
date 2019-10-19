from flask import render_template, url_for, redirect, Flask, render_template, request, session
import json

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
            radius = request.form['field3']
            search_criteria = [latitude, longitude, radius]
            # book_list = get_book([latitude, longitude, radius])
            book_list = [{"address":"street1","name":"best rest"}]
            print(search_criteria)
            return render_template("restaurantList.html", results=book_list)
    else:
        book_list = [{"address":"street1","name":"best rest"}]
        return render_template("restaurantList.html", results=book_list)

if __name__ == '__main__':
    app.run()
