import math 
from numpy import *
from scipy.optimize import *
import matplotlib.pyplot as plt

#Constants
#----------------------------------------------------------------------------
L1 = 400 #link 1 is 400mm
L2 = 315 #link 2 is 315mm
#--------------------------------------------------------------------------------

#Compute 2D IK takes (x,y) coords and returns theta1 and theta2 angles
#---------------------------------------------------------------------------------------------------
def InvKine_2D(x,y): 
    def Compute_IK(z):   
        L1 = 400 #link 1 is 400mm
        L2 = 315 #link 2 is 315mm
        theta2 = z[0]    
        theta1 = z[1]
        F = empty((2))    
        F[0] = (pow(x,2)+pow(y,2)-pow(L1,2)-pow(L2,2))/(2*L1*L2) - math.cos(theta2)  #cosine(theta2)  
        F[1] = math.atan2(y,x) - math.atan2(L2*math.sin(theta2),L1 + L2*math.cos(theta2)) - theta1    #
        return F
        
    z = fsolve(Compute_IK, [1,1]) #fsolve with a guess
    theta_2 = z[0]*(180/pi)
    theta_1 = z[1]*(180/pi)
    return [theta_2, theta_1]   #return angles as list

#angles = InvKine_2D(600,0)      #angles from (x,y)
#print(angles[0])                #print first element of angles list

#------------------------------------------------------------------------------------------------------
