import requests
import datetime
import bluetooth
#unfortunately we had to find bluetooth devices instead of advertising a service
#because the library that supports this functionality for python is broken :(
HARD_CODED_MAPPING = {
    "Bose SLIII": "Garage",
    "Aukey EP-B4": "Kitchen"
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
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
def poll_for_devices(doctor):
    #if device found update location and send timestamp
    devices = bluetooth.discover_devices(lookup_names=True, flush_cache=True, duration=5)
    print(devices)
    print("found {} devices".format(len(devices)))
    for name in devices:
        location = HARD_CODED_MAPPING.get(name[1])
        if location is not None:
            print("Updated {}'s location to {}".format(doctor, location))
            update_location(doctor, location)
    print("Done polling")