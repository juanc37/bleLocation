from flask import Flask
from flask import request
app = Flask(__name__)
import datetime

locations_db = {}
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
            doctor = locations_db.get(request.form['doctor_id'])
        else:
            raise Exception("Invalid Request")
    except Exception as e:
        print(e)
        error = e
    if doctor is None:
        return "This doctor is not able to be located currently"
    return doctor


if __name__ == '__main__':
    app.run()
