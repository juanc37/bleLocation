#!/usr/bin/env python3
"""PyBluez ble example beacon.py
Advertises a bluethooth low energy beacon for 15 seconds.
"""
import time

import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
bluetooth.advertise_service(sock, 'Location Hub', description='garage')

while True:
    pass

