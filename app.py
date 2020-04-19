import os
import datetime 
#request for usage of POST and GET request. Needed to POST data from HTML form
#render_template allows to redirect to html in flask instead of writing it in .py file
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

locations_db = {}

#testing dipalying name 
doctorName = ''
doctor = ''

#this is tue home page and calls index.html
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/helloDoc", methods=['GET', 'POST'])
def helloDoc():
    if request.method == 'POST':
        doctorName= request.form['doctor_id']
        
    return render_template('index.html', doctorName=doctorName)

@app.route('/update-location',methods=["POST"])
def update_location():
    error = ''
    update_time = datetime.datetime.now
    try:

        if request.method == "POST":
            doctor = request.form['doctor_id']
            new_location = request.form['new_location']
            locations_db[doctor] = {
                "location": new_location,
                "updated": update_time
            }
        else:
            raise Exception("Invalid Request")

    except Exception as e:
        print(e)
        error = e
        return 'Not Updated'

    return 'Updated'

@app.route('/sign-off',methods=["POST"])
def sign_off():
    error = ''
    try:

        if request.method == "POST":
            doctor = request.form['doctor_id']
            locations_db.pop(doctor)
        else:
            raise Exception("Invalid Request")

    except Exception as e:
        print(e)
        error = e
        return 'Not Signed Off'

    return 'Signed Off'

@app.route('/locate',methods=["POST"])
def locate():
    error = ''
    try:
        if request.method == "POST":
            doctorName= request.form['doctor_id']
            doctor = locations_db.get(request.form['doctor_id'])
        else:
            raise Exception("Invalid Request")
    except Exception as e:
        print(e)
        error = e
    if doctor is None:
        return render_template('index.html', doctorName=doctorName, doctor= "This doctor is not able to be located currently")
    return render_template('index.html', doctorName=doctorName, doctor= doctor)

if __name__ == "__main__":
    app.run()
    