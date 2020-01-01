# 3R Planar Robot For 2D Shape Drawing 
# Project Overview
The project serves as a demonstration of [Newton-Raphson inverse kinematics algorithm](https://en.wikipedia.org/wiki/Newton%27s_method). In this project, any shape within its workspace of the 3R arm can be drawn. An example curve, [the heart curve](http://mathworld.wolfram.com/HeartCurve.html), is stored in the parameter server. You can put in any parametric functions
of a single continuous shape, please see below for more details.

The design and the workspace of the robot are shown below  


![Screenshot from 2019-12-30 21-18-44](https://user-images.githubusercontent.com/39393023/71608911-0c2be900-2b4a-11ea-8b23-0e264bd6ae2c.png)

![Screenshot from 2019-12-30 16-21-04](https://user-images.githubusercontent.com/39393023/71603023-952e2a80-2b20-11ea-8494-e804d4c4b106.png)



##### Demonstration
[![Screenshot from 2019-12-13 13-39-59](https://user-images.githubusercontent.com/39393023/70827219-61c46f80-1dae-11ea-81c7-01a2741d246f.png)](https://youtu.be/J4vcd4qHMO0)



## How to Use This Code
- To install this package, on your local computer, Run 
```
$ mkdir -p robot_arm_simulations/src
$ cd robot_arm_simulations/src
$ git clone git@github.com:RicoJia/Robot_Arm_Simulations.git
$ cd ..
$ catkin_make 
```
-  To see visualize the trajectory on Rviz using marker, run

```
$ roslaunch robot_arm_simulation robot_arms_marker_included.launch
```

For showing the robot's movement only, run
```
'''
$ roslaunch robot_arm_simulation robot_arms_marker_included.launch marker_status:=false
```


## Code Overview
#### 2D Newton Raphson Inverse Kinematics Algorithm

This part was built for 2D planar inverse kinematics problem, using screw representation of robot joints. 
The inputs to this part are:
1. M - Home position of the robot (when all joint angles are zero)
2. blist - Joint Screw axes in the end effector body frame
3. Tsd - Desired end effector transformation in Lie Group SE(2)
4. thetalist0 - Current joint angles
5. e_theta - Orientation error tolerance between the end result and the desired end effector transformation Tsd. Default value is 0.01rad
6. e_v - Distance Error tolerance between the end result and the end effector transformation Tsd. The default value is 0.001

 the board) is set by using a simple P controller as follows:

The outputs from this part are:
1. success - True if a solution is found, otherwise false
2. thetalist_new - Joint angles from the furthest joint to the closest joint to the end effector

## Changing the Shape to Draw

To change the shape to draw, simply go to ```robot_arm_simulation``` file under
```src``` directory. Find **TRAJECTORY_X** and **TRAJECTORY_Y**, and put your full list of trajectory
points as a numpy array there. 
