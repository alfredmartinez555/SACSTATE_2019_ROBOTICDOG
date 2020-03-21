import math as m
import numpy as np
import matplotlib.pyplot as plt
##
# these values correspond to the triangles in each joint
a_thigh = 94 
a_knee  = 95
c_thigh = 162
c_knee  = 169

# max distance (mm) from tof sensor 
max_thigh = 85
max_knee  = 149
min_thigh = 28
min_knee  = 10

# Limb Lengths
knee_foot_length = 352
hip_knee_length  = 355

# theta is the specified / desired angle
def Knee_Angle_To_Distance(theta): 
    theta = m.radians(theta)   
    alpha_knee = m.asin((a_knee/c_knee)*m.sin(theta))
    beta_knee  = 180-m.degrees(alpha_knee)-m.degrees(theta)
    b_knee     = c_knee*(m.sin(m.radians(beta_knee))/m.sin(theta))
    dist_knee  = max_knee - b_knee + 95
    return dist_knee

def Thigh_Angle_To_Distance(theta):
    theta = m.radians(theta)
    alpha_thigh = m.asin((a_thigh/c_thigh)*m.sin(theta))
    beta_thigh  = 180-m.degrees(alpha_thigh)-m.degrees(theta)
    b_thigh     = c_thigh*(m.sin(m.radians(beta_thigh))/m.sin(theta))
    dist_thigh  = max_thigh - b_thigh + 190
    return dist_thigh
