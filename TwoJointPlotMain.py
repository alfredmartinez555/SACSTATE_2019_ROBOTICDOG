from TwoJointPlotImport import TwoLinkArm
from math import cos, sin, sqrt
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.axes

plt.ion()

arm = TwoLinkArm()
arm.link_lengths = [72.35, 88.9]


UserInputTheta1 = 135
UserInputTheta2 = 90


theta0 = math.radians(UserInputTheta1)-math.pi
theta1 = math.radians(UserInputTheta2)-math.pi/2


arm.update_joints([theta0, theta1])
arm.plot()

def transform_points(points, theta, origin):
    T = np.array([[cos(theta), -sin(theta), origin[0]],
                  [sin(theta), cos(theta), origin[1]],
                  [0, 0, 1]])
    return np.matmul(T, np.array(points))

def draw_angle(angle, offset=0, origin=[0, 0], r=0.5, n_points=100):
        x_start = r*cos(angle)
        x_end = r
        dx = (x_end - x_start)/(n_points-1)
        coords = [[0 for _ in range(n_points)] for _ in range(3)]
        x = x_start
        for i in range(n_points-1):
            y = sqrt(r**2 - x**2)
            coords[0][i] = x
            coords[1][i] = y
            coords[2][i] = 1
            x += dx
        coords[0][-1] = r
        coords[2][-1] = 1
        coords = transform_points(coords, offset, origin)
        plt.plot(coords[0], coords[1], 'k-')

def plot_diagram():
    plt.plot([0, 0.5], [0, 0], 'k--')
    plt.plot([arm.elbow[0], arm.elbow[0]+0.5*cos(theta0)],
             [arm.elbow[1], arm.elbow[1]+0.5*sin(theta0)],
             'k--') 

    plt.plot([-161.25,161.25],[0,0])
    circle1 = patches.Arc(xy=(0,0), width=2*72.35, height=2*72.35, theta1=180, theta2=0)
    plt.gca().add_patch(circle1)

    circle2 = patches.Arc(xy=(0,0), width=2*161.25, height=2*161.25, theta1=180, theta2=0)
    plt.gca().add_patch(circle2)

    #plt.annotate(r"$\theta_0$", xy=(20,-15), size=15)
    #plt.annotate(r"$\theta_1$", xy=(arm.elbow[0]+5,arm.elbow[1]+5), size=15)

    plt.annotate("Shoulder", xy=(arm.shoulder[0], arm.shoulder[1]),
                xytext=(arm.shoulder[0]+25, arm.shoulder[1]+25),
                arrowprops=dict(facecolor='black', shrink=0.05))

    plt.annotate("Elbow", xy=(arm.elbow[0], arm.elbow[1]), 
                xytext=(arm.elbow[0]+25,arm.elbow[1]+25),
                arrowprops=dict(facecolor='black', shrink=0.05))

    plt.annotate("Wrist", xy=(arm.wrist[0], arm.wrist[1]), 
                xytext=(arm.wrist[0]+25, arm.wrist[1]+25),
                arrowprops=dict(facecolor='black', shrink=0.05))

    plt.axis("equal")  

    plt.show()

def plot_angle(theta0, theta1):
    theta0 = (theta0)-math.pi
    theta1 = (theta1)-math.pi/2

    arm.update_joints([theta0,theta1])
    plt.cla()
    arm.plot()
    plot_diagram()
    plt.pause(0.01)

def user_input_angle():
    theta0 = input("Input Theta 0: ")
    print("Theta 0: ", theta0)
    theta0 = math.radians(int(theta0))

    theta1 = input("Input Theta 1: ")
    print("Theta 1: ", theta1)
    theta1 = math.radians(int(theta1))
    return theta0, theta1


def main():
    while 1:
        theta0, theta1 = user_input_angle()
        plot_angle(theta0, theta1)
    


    #end main
    
   
if __name__ == "__main__":
    main()
