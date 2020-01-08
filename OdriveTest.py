#!/usr/bin/env python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""
from __future__ import print_function
import odrive
from odrive.enums import *
import time
import math
##
print("finding an odrive...")
odrive0 = odrive.find_any(serial_number = "20623599524B")
print("1st odrive found")
odrive1 = odrive.find_any(serial_number = "206E39864D4D")
print("2nd odrive found")
odrive2 = odrive.find_any(serial_number = "207739874D4D")
print("3rd odrive found")
odrive3 = odrive.find_any(serial_number = "207D39874D4D")
print("4th odrive found")
##
print("starting calibration...")
odrive0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
odrive1.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
odrive2.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
odrive3.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

##
while odrive0.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
while odrive1.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
while odrive2.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
while odrive3.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
##
odrive0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrive1.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrive2.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrive3.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
##
t0 = time.monotonic()
while True:
    print("1:" + str(odrive0.vbus_voltage))
    print("2:" + str(odrive1.vbus_voltage))
    print("3:" + str(odrive2.vbus_voltage))
    print("4:" + str(odrive3.vbus_voltage))
    time.sleep(0.0000001)

