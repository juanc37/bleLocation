#!/usr/bin/env python3
"""PyBluez ble example beacon.py
Advertises a bluethooth low energy beacon for 15 seconds.
"""
import time

import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sock.bind(("", 0))
sock.listen(0)

bluetooth.advertise_service(sock, 'Location Hub', description='garage')

# while True:
#     time.sleep(1)

