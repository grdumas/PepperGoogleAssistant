# play_response.py
This script directs a Pepper robot to play an audio file containing the response of Google Assistant.

## sys.path.append(...)
Adds the NAOqi Python SDK to the PATH. 

### Example
```
sys.path.append('/home/user/pynaoqi/lib/python2.7/site-packages')
```
* Replace '/home/user/pynaoqi/lib/python2.7/site-packages' with the filepath where your NAOqi Python SDK is stored.

---

## Pepper object
* Stores the IP address of the Pepper robot as a string.
* To find your Pepper's IP, press the circular button on the front of the robot's chassis, beneath its tablet. 

### Example
```
pepper = '192.168.1.140'
```

---

## ALProxy object
ALProxy object allows the creation of a proxy to a NAOqi module

### Syntax
```
ALProxy(name, ip, port)
```
* *name* The name of the module
* *ip* The IP address of the robot
* *port* The network port to access on the robot. Default is 9559.

---

## playFile() method
Begin playing a specified file on Pepper.

### Syntax
```
object.playFile(filename)
```
* *filename* Is the absolute path of the audio file.

### Example
```
audio.playFile("/home/nao/syn.wav")
```