import sys

sys.path.append('/home/gdumas/pynaoqi/lib/python2.7/site-packages')

from naoqi import ALProxy
pepper = '192.168.1.140'
audio = ALProxy("ALAudioPlayer", pepper, 9559)
audio.playFile("/home/nao/syn.wav")

