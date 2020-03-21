#from adafruit_servokit import ServoKit
import time
import numpy as np
import math as m

def inverseKin2D(x,y):
    #Calculate Angles
    link = np.array([352, 355]) #thigh, foot
    theta2 = m.acos((m.pow(x, 2)+m.pow(y,2)-m.pow(link[0],2)-m.pow(link[1],2))/(2*link[0]*link[1]))
    theta1 = m.atan2(y,x)- m.atan2((link[1]*m.sin(theta2)),(link[0]+(link[1]*m.cos(theta2))))
    #x,y =>>>> theta1, theta2
    #print(x, y, round(m.degrees(theta1),2), round(m.degrees(theta2),2))

    return [m.degrees(theta2),m.degrees(theta1)]

print(inverseKin2D(200,200))
