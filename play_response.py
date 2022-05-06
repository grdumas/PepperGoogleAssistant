"""@package docstring
Documentation for this module.

More details.
"""

import sys
"""Note: change the following filepath to match the location of the Pynaoqi SDK on your system"""
sys.path.append('/home/gdumas/pynaoqi/lib/python2.7/site-packages')

from naoqi import ALProxy

## Pepper object
#
# Stores the IP address of the Pepper robot as a string.
# To find your Pepper's IP, press the circular button on the front of the robot's chassis, beneath its tablet. 
pepper = '192.168.1.140'

## Documentation for ALProxy object
#
# ALProxy object allows the creation of a proxy to a module
#
# syntax is ALProxy(name, ip, port)
# @param name The name of the module
# @param ip The IP address of the robot
# @param port The network port to access on the robot. Default is 9559
audio = ALProxy("ALAudioPlayer", pepper, 9559)

## Documentation of playFile() method
#
# Begin playing a specified file
#
# syntax is object.playFile(filename)
# @param filename Is the absolute path of the file
audio.playFile("/home/nao/syn.wav")

