
import time
import board
import busio
import adafruit_vl6180x
import adafruit_tca9548a

#struct library (used for byte conversions)
import struct


#I2C Bus Initialization
i2c = busio.I2C(board.SCL, board.SDA, frequency=5000000)

#MUX Object
tca = adafruit_tca9548a.TCA9548A(i2c)

#Sensors to be MUXed
#mpu = adafruit_mpu6050.MPU6050(tca[7])
tof_1 = adafruit_vl6180x.VL6180X(tca[7]) #changed from [1]

while True:
    count = 0
    lst = []
    #convert to inches from mm
    mm_range = tof_1.range
    in_range = mm_range*0.0393701
    count = count + 1
    lst.append(mm_range)
    print("Range in mm: " + str(mm_range))
    print("Range in inches: " + str(in_range))
    time.sleep(0.5)

