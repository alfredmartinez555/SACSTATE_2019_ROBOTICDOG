import math
import time
from numpy import *
from Dist_to_Angle import dist_angle_foot
from Inv_Kinematics import InvKine_2D

#Constants
#----------------------------------------------------------------------------

def EllipseGait2D(h,k,a,b,stepsize):
    for i in range(0,360,stepsize):     #loop 0 to 360 in steps of "stepsize"
        i = stepsize + i
        delta_x = a*math.cos(i*(pi/180)) + h
        delta_y = b*math.sin(i*(pi/180)) + k

        Thetas = InvKine_2D(delta_x,delta_y)

        print("Changing x coord: ",delta_x)
        print("Changing Theta 2: ", Thetas[0])
        print("Changing y coord: ",delta_y)
        print("Changing Theta 1: ", Thetas[1],"\n")

        #Get ball screw carriage distance using dist_angle_foot
        #---------------------------------------------------------------------
        foot_Distance = dist_angle_foot(Thetas[0])      #get theta 2 for end-effector position
        thigh_Distance = dist_angle_foot(Thetas[1])     #get theta 1 for thigh position
        #----------------------------------------------------------------

        #Motor control using distances
        #-------------------------------------------------------------

        #--------------------------------------------------------------

EllipseGait2D(150,150,100,150,1)
