#!/usr/bin/python
import math
import numpy as np

def SO2_2_theta(R):
    """
    Input R is SO2 Rotation matrix.
    Sample Input: [[cos(theta) -sin(theta)],
        [sin(theta) cos(theta)]]
        Output is the angle of R
    Sample output: theta = pi/2
    """
    R = np.array(R)
    theta = math.atan2(R[1,0], R[0,0])
    return theta

def theta_2_SO2(theta):
    """
    Input theta is a scalar vector
    Output: SO2 Rotation matrix
    """
    c = math.cos(theta)
    s = math.sin(theta)
    R = np.array([[c, -s],
                  [s, c]])
    return R

def vec_2_SE2(v):
    """
    Input: twist in unit time [theta, x, y]
    Output: SO2
    """
    theta = v[0]
    x = v[1]
    y = v[2]
    R = theta_2_SO2(theta)
    T = np.vstack([np.hstack([R, np.array([[x], [y]])]), np.array([[0, 0, 1]]) ])
    return T

def SE2_2_vec(T):
    """
    Input: SO2
    Output: twist in unit time [theta, x, y]
    """
    T = np.copy(T)
    theta = v[0]
    x = v[1]
    y = v[2]
    R = theta_2_SO2(theta)
    T = np.vstack([np.hstack([R, np.array([[x], [y]])]), np.array([[0, 0, 1]]) ])
    return T



