#Working Code
import time
import board
import busio

# Serial library
import serial

#Sensor Libraries
import adafruit_mpu6050
import adafruit_vl6180x

#MUX Library
import adafruit_tca9548a

#struct library (used for byte conversions)
import struct

#Odrive Library
import odrive
from odrive.enums import *

#I2C Bus Initialization
i2c = busio.I2C(board.SCL, board.SDA, frequency=5000000)

#MUX Object
tca = adafruit_tca9548a.TCA9548A(i2c)

#Sensors to be MUXed
#mpu = adafruit_mpu6050.MPU6050(tca[7])
tof_1 = adafruit_vl6180x.VL6180X(tca[1])
tof_2 = adafruit_vl6180x.VL6180X(tca[7])


#--------------------------------------------------------------------
#2/4 Odrive 
print("finding an odrive...")
my_drive = odrive.find_any(serial_number = "20623599524B")
time.sleep(0.1)

# # Full Calibration
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

# # Velocity Config
my_drive.axis0.controller.config.vel_limit = 130000
my_drive.axis1.controller.config.vel_limit = 130000


while (my_drive.axis0.current_state != AXIS_STATE_IDLE and my_drive.axis1.current_state != AXIS_STATE_IDLE):
    time.sleep(0.1)
print('done')
my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
print('In Closed Loop...')
time.sleep(1)
#--------------------------------------------------------------------

#------------------------------------------------------------------
# 2/17 Mon: Motor Setpoint Function
motor_1 = 0
def motorSetpoint(requested_distance):
    global motor_1
    if tof_1.range > requested_distance:
        #postive set point
        print('positive')
        print(my_drive.axis0.controller.pos_setpoint)

        if abs(tof_1.range - requested_distance) < 3:
            my_drive.axis0.controller.pos_setpoint = motor_1
        else:
            motor_1 = motor_1 + 2500
            my_drive.axis0.controller.pos_setpoint = motor_1
        time.sleep(0.01)

    if tof_1.range < requested_distance:
        print('negative')
        print(my_drive.axis0.controller.pos_setpoint)

        if abs(tof_1.range - requested_distance) < 3:
            my_drive.axis0.controller.pos_setpoint = motor_1
            print('less than 3mm away')
        else:
            motor_1 = motor_1 - 2500
            my_drive.axis0.controller.pos_setpoint = motor_1
            print('more than 3mm away')
        time.sleep(0.01)

motor_0 = 0
def motorSetpoint_axis1(requested_distance):
    global motor_0
    if tof_2.range > requested_distance:
        #postive set point
        print('Thigh TOF: ', str(tof_2.range))
        print(my_drive.axis1.controller.pos_setpoint)

        if abs(tof_2.range - requested_distance) < 3:
            my_drive.axis1.controller.pos_setpoint = motor_0
        else:
            motor_0 = motor_0 + 2500
            my_drive.axis1.controller.pos_setpoint = motor_0
        time.sleep(0.01)

    if tof_2.range < requested_distance:
        print('Thight TOF: ', str(tof_2.range))
        print(my_drive.axis1.controller.pos_setpoint)

        if abs(tof_2.range - requested_distance) < 3:
            my_drive.axis1.controller.pos_setpoint = motor_0
            print('less than 3mm away')
        else:
            motor_0 = motor_0 - 2500     
            my_drive.axis1.controller.pos_setpoint = motor_0
            print('more than 3mm away')
        time.sleep(0.01)
#---------------------------------------------------------------------

while True:
    #mm_range = str(tof_1.range) + "\n"
    #convert to inches from mm
    #in_range = str(mm_range*0.0393701)
    
    #print("Range in mm: " + str(mm_range))
    #print("Range in inches: " + str(in_range))
    #print("Acceleration: X:%f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    #print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    #print("Temperature: %.2f C\n"%(mpu.temperature))
    #time.sleep(0.1)

#---------------------------------------------------------------------
# 2/4 Odrive Algorithm
    
    print("Knee TOF Range: ", tof_1.range)
    print("Thigh TOF Range: ", tof_2.range)
    motorSetpoint_axis1(30)
    motorSetpoint(110)


#-------------------------------------------------------------------
#         
#------------------------------------------------------------------
#    #2/3 Filtering TOF data
#    for i in range(5):
#        #print(i)
#        filter_data_1[i] = tof_1.range
#        filter_data_2[i] = tof_2.range
#
#        print("Data: " + str(filter_data_1[i]))
#        print("Data: " + str(filter_data_2[i]))
#        time.sleep(1)
#        if i == 4:
#            average_1 = (sum(filter_data_1))/5
#            average_2 = (sum(filter_data_2))/5
#            #serial_port.write(str(average).encode())
#            print(average_1)
#            print(average_2)
#            #serial_port.write(struct.pack('f', average))
    #------------------------------------------------------------------

    #-----------------------------------------------------------------
    #1/28 Serial comm
    #serial_port.write(mm_range.encode())
    #print("sending: " + mm_range)
    #------------------------------------------------------------------
