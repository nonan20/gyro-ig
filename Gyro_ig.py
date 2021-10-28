
#importing basic modules, this is meant for spike prime so you would change what ur importing for ev3 
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
#basic python library so keep this :/
from math import *

#const variable, you could delete this entirely or just translate it for ev3
hub = PrimeHub()

#defining motor ports idk the function for ev3 so you would change that
motor_pair = MotorPair('A', 'E')

#resetting the gyro sensor so that it defines the current angle (whatever angle you want it to drive at) as 0.
#On spike prime the gyro is atatched to the hub so the entire command would be different on an ev3 bot
hub.motion_sensor.reset_yaw_angle()

#this loop is whats doing all the work, its currently a forever loop
#you would want to change this to a recursive loop and make it interrupt after a certain amount of time or you could have it stop when lightsensor finds a certain value
#you could also take into account that the lego robotics motors work as a stepper motor and then take the current motor position to set up a recursive loop till it detects x rotations have been done
while True:
    #setting up a variable named error that contains the current gyro position at any given moment ((NOT A LIST SO DONT GO ABOUT TRYING TO INDEX IT FOR OLD VALUES))
    error = hub.motion_sensor.get_yaw_angle()
    #setting up a variable that stores the value the robot needs to move at to quickly correct itself, basically this value is meant to negate the error
    correction = error * -2
    #moving using tank control and having the wheels rotate at different speeds and directions to correct the error
    motor_pair.start_tank(int(60+correction), int(60-correction))






#good luck, and dm me on discord if you need anything :D (nonan20#3771) 
