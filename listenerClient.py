import time
import bluetooth_updater


while True:
    bluetooth_updater.poll_for_devices("Juan Candelaria Claborne")
    time.sleep(10)
