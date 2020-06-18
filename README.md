# Aim
This algorithm calculates and sends the throttle, pitch and rudder values to an underwater robot using the values from a joystick as an input. These values along with status of other buttons is displayed using a GUI

# Motivation
This algorithm was developed for [MATE ROV International Competition 2016/17](https://materovcompetition.org/).The GUI developed aids the pilot in controlling and monitoring the underwater robot. To move the ROV in 3 degrees of freedom, the values from the Joystick(the controller for the robot) were mapped to calculate the speed and direction of individual thrusters using vectorisation. A total of eight thrusters were used to control the movement of the robot.

# Structure of Folder
1. 'Joystick_RollingTrigger.py': Main algorithm
2. 'GUI.png': Image of the GUI

# Setup/ Installation
```
pip3 install opencv-python
pip3 install opencv-contrib-python
```
Note: This algorithm uses 'pygame' and hence requires to physically connect a joystick to your computer to run successfully

# Pilot GUI
![Pilot GUI](https://user-images.githubusercontent.com/34181525/85006282-d3141f00-b151-11ea-9fea-9e52ea5ab573.png)
