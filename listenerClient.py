import time
import bluetooth_updater


while True:
    time.sleep(10)
    print(bluetooth_updater.poll_for_devices())
