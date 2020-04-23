import requests
import datetime
import bluetooth
HARD_CODED_MAPPING = {
    "Bose SLIII": "wow"
}
# api-endpoint
URL = "http://127.0.0.1:5000/update-location"


def update_location(doctor, location):
    # defining a params dict for the parameters to be sent to the API
    DATA = {
        "located": doctor,
        "new_location": location,
    }
    # sending get request and saving the response as response object
    r = requests.post(url=URL, data=DATA)

def poll_for_devices():
    #if device found update location and send timestamp
    devices = bluetooth.find_service(name='Location Hub', uuid=None, address=None)
    #nearby_devices = bluetooth.discover_devices(lookup_names=True, flush_cache=True, duration=20)
    #print"found %d devices" % len(nearby_devices)
    for name in devices.description:
        location = HARD_CODED_MAPPING.get(name)
        if location is not None:
            update_location(location)
        print("%s - %s" % (name))


