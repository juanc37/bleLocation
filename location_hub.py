#!/usr/bin/env python3
"""PyBluez ble example beacon.py
Advertises a bluethooth low energy beacon for 15 seconds.
"""
import time

import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.bind(("", bluetooth.PORT_ANY))
sock.listen(1)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
# service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
#                             profiles=[bluetooth.SERIAL_PORT_PROFILE],
#                             # protocols=[bluetooth.OBEX_UUID]
#                             )

bluetooth.advertise_service(sock=sock,
                            name='Location Hub',
                            description='garage',
                            service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

# while True:
#     time.sleep(1)

