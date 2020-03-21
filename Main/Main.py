import time
from numpy import *
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
from Angle_to_Dist import dist_angle_foot
from Inv_Kinematics import InvKine_2D
from Inve import inverseKin2D
from big_leg import  Knee_Angle_To_Distance, Thigh_Angle_To_Distance

#Constants
#----------------------------------------------------------------------------
#I2C Bus Initialization
i2c = busio.I2C(board.SCL, board.SDA, frequency=5000000)

#MUX Object
tca = adafruit_tca9548a.TCA9548A(i2c)

#Sensors to be MUXed
#mpu = adafruit_mpu6050.MPU6050(tca[7])
tof_2 = adafruit_vl6180x.VL6180X(tca[7])
tof_1 = adafruit_vl6180x.VL6180X(tca[1])

#Calibrate Motor
#--------------------------------------------------------------
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
#----------------------------------------------------------------------

# Motor Setpoint Function Axis0
#----------------------------------------------------------------------
motor_0 = 0
def motorSetpoint_axis0(requested_distance):
    global motor_0
    if tof_1.range > requested_distance:
        #postive set point
        print('Knee TOF: ', str(tof_1.range))
        print(my_drive.axis0.controller.pos_setpoint)

        if abs(tof_1.range - requested_distance) < 3:
            my_drive.axis0.controller.pos_setpoint = motor_0
        else:
            motor_0 = motor_0 + 3500
            my_drive.axis0.controller.pos_setpoint = motor_0
        time.sleep(0.01)

    if tof_1.range < requested_distance:
        #negative set point
        print('Knee TOF: ', str(tof_1.range))
        print(my_drive.axis0.controller.pos_setpoint)

        if abs(tof_1.range - requested_distance) < 3:
            my_drive.axis0.controller.pos_setpoint = motor_0
            print('less than 3mm away')
        else:
            motor_0 = motor_0 - 3500
            my_drive.axis0.controller.pos_setpoint = motor_0
            print('more than 3mm away')
        time.sleep(0.01)
#----------------------------------------------------------------------

# Motor Setpoint Function Axis1
#----------------------------------------------------------------------
motor_1 = 0
def motorSetpoint_axis1(requested_distance):
    global motor_1
    if tof_2.range > requested_distance:
        #postive set point
        print('Thigh TOF: ', str(tof_2.range))
        print(my_drive.axis1.controller.pos_setpoint)

        if abs(tof_2.range - requested_distance) < 3:
            my_drive.axis1.controller.pos_setpoint = motor_1
        else:
            motor_1 = motor_1 + 3500
            my_drive.axis1.controller.pos_setpoint = motor_1
        time.sleep(0.01)

    if tof_2.range < requested_distance:
        print('Thight TOF: ', str(tof_2.range))
        print(my_drive.axis1.controller.pos_setpoint)

        if abs(tof_2.range - requested_distance) < 3:
            my_drive.axis1.controller.pos_setpoint = motor_1
            print('less than 3mm away')
        else:
            motor_1 = motor_1 - 3500     #was 2500
            my_drive.axis1.controller.pos_setpoint = motor_1
            print('more than 3mm away')
        time.sleep(0.01)
#----------------------------------------------------------------------

# Ellipse Gait Function
#---------------------------------------------------------------------------------
def EllipseGait2D(h,k,a,b,stepsize):
    for i in range(0,360,stepsize):     #loop 0 to 360 in steps of "stepsize"
        i = stepsize + i
        delta_x = a*math.cos(i*(pi/180)) + h
        delta_y = b*math.sin(i*(pi/180)) + k

        #Thetas = InvKine_2D(delta_x,delta_y)
        Thetas = inverseKin2D(delta_x,delta_y)


        print("Changing x coord: ",delta_x)
        print("Changing Theta 2: ", Thetas[0])
        print("Changing y coord: ",delta_y)
        print("Changing Theta 1: ", Thetas[1],"\n")

        #Get ball screw carriage distance using dist_angle_foot
        #---------------------------------------------------------------------
        foot_Distance = AngleToDistance(Thetas[0])      #get theta 2 for end-effector position
        #thigh_Distance = dist_angle_foot(Thetas[1])    #get theta 1 for thigh position
        #----------------------------------------------------------------

        #Motor control using distances
        #-------------------------------------------------------------
        motorSetpoint_axis0(foot_Distance)
        #motorSetpoint_axis1(thigh_Distance)
        #--------------------------------------------------------------
        #time.sleep(0.5)

#------------------------------------------------------------------------------------
while True:

    #EllipseGait2D(300,400,10,10,1)
    
    foot_Distance = Knee_Angle_To_Distance(45)
    print("foot distance: ", foot_Distance)
    motorSetpoint_axis0(foot_Distance)

    thigh_Distance = Thigh_Angle_To_Distance(80)
    print("Thigh distance: ", thigh_Distance)
    motorSetpoint_axis1(thigh_Distance)
    #time.sleep(0.25)
