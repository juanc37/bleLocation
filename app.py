from flask import Flask
from flask import request
app = Flask(__name__)

locationsDB = {}
@app.route('/update-location',methods=["POST"])
def update_location():
    error = ''
    try:

        if request.method == "POST":
            doctor = request.form['doctor_id']
            new_location = request.form['new_location']
            locationsDB[doctor] = new_location
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
            locationsDB.pop(doctor)
        else:
            raise Exception("Invalid Request")

    except Exception as e:
        print(e)
        error = e
        return 'Not Signed Off'

    return 'Signed Off'



if __name__ == '__main__':
    app.run()
