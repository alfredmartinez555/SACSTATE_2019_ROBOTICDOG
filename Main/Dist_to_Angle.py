import math

def dist_angle_foot(theta):

    #length constants
    a = 97  
    c = 138

    #max distance (mm) from tof sensor 
    max = 149 

    #calculate/return distance required to achieve requested angle
    distance = max - (a*math.cos(theta)) - (math.sqrt((math.pow(a,2))*(math.cos(theta)**2) - math.pow(a,2) + math.pow(c,2)))

    return distance

#print(dist_from_angle(90))
