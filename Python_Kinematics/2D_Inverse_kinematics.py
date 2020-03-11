import math 
from numpy import * 
from scipy.optimize import * 
import matplotlib.pyplot as plt
#for positive sin theta 2 
theta_2 = math.atan2(math.sqrt(0.7623),-0.4875) 
theta_1 = math.atan2(0.5,0.5) - math.atan2(0.5*math.sqrt(0.7623),0.8+(0.5*(-.4875)))
#for negative sin theta 2 
theta_2n = math.atan2(-1*math.sqrt(0.7623),-0.4875) 
theta_1n = math.atan2(0.5,0.5) - math.atan2(0.5*-1*math.sqrt(0.7623),0.8+(0.5*(-.4875)))

#!Python NonLinear Equations using fsolve 
#---------------------------------------------------------------------------------------------------
def firstFunction(z):    
  theta2 = z[0];    
  theta1 = z[1];
  F = empty((2))    
  F[0] = (pow(0.5,2)+pow(0.5,2)-pow(0.8,2)-pow(0.5,2))/(2*0.8*0.5) - math.cos(theta2)    
  F[1] = math.atan2(0.5,0.5) - math.atan2(0.5*math.sin(theta2),0.8 + 0.5*math.cos(theta2)) - theta1    
  return F 
fGuess = array([1,1]) 
z = fsolve(firstFunction, fGuess)

def secondFunction(x):    thetatwo = x[0];    thetaone = x[1];
    Y = empty((2))    
    Y[0] = (pow(0.5,2)+pow(0.5,2)-pow(0.8,2)-pow(0.5,2))/(2*0.8*0.5) - math.cos(thetatwo)    
    Y[1] = math.atan2(0.5,0.5) - math.atan2(0.5*math.sin(thetatwo),0.8 + 0.5*math.cos(thetatwo)) - thetaone    
    return Y 
sGuess = array([-1,5]) 
x = fsolve(secondFunction,sGuess)
#------------------------------------------------------------------------------------------------------

#Python Calculated Answers with fsolve
#----------------------------------------------------------------------------------------
print ("Python Calcluated Answers using fsolve") 
print ("Theta 2 with initial guess 1:",math.degrees(z[0]),"degrees") 
print ("Theta 1 with initial guess 1:",math.degrees(z[1]),"degrees\n") 
print ("Theta 2 with initial guess -1:",math.degrees(x[0]),"degrees") 
print ("Theta 1 with inital guess 5:",math.degrees(x[1]),"degrees")
#-------------------------------------------------------------------------------------

#hand calculated answers 
print ("For positive sin theta 2") 
print ("Theta 2 = ",math.degrees(theta_2),"degrees") 
print ("Theta 1 = ",math.degrees(theta_1),"degrees\n") 
print ("For negative sin theta 2") 
print ("Theta 2 = ",math.degrees(theta_2n),"degrees") 
print ("Theta 1 = ",math.degrees(theta_1n),"degrees\n")
