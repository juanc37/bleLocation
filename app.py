import os
import datetime 
#request for usage of POST and GET request. Needed to POST data from HTML form
#render_template allows to redirect to html in flask instead of writing it in .py file
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#hardcoded database; change later when bluetooth is connected
locations_db = {
    "Cesar Lopez" : "Love Library",
   "Juan Candelaria Claborne" : "Garage",
   "Sami Quiroz" : "GMCS425",
   "Matthew Rose": "Eureka",
   "Daniel Valoria" : "Music Room",
   "Jasmine Nelson" : "Seattle"
}

#testing dipalying name 
doctorName = ''
location = ''

#this is the home page and calls index.html
@app.route("/")
def hello():
    return render_template('index.html')

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
            location = locations_db.get(doctorName)
        else:
            raise Exception("Invalid Request")
    except Exception as e:
        print(e)
        error = e
    if location is None:
        return render_template('locate.html', doctorName=doctorName, location= "This doctor is not able to be located currently")
    return render_template('locate.html', doctorName=doctorName, location= location)

if __name__ == "__main__":
    app.run()
    