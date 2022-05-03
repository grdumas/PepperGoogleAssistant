# Installation and Setup

## Development Environment
### Operating System (OS)
This project was developed on a workstation running [Ubuntu 16.04 Xenial Xerus](https://ubuntu.com/16-04) in the interest of compatibility with SoftBank software. To download, please see the [ubuntu releases website](https://releases.ubuntu.com/). The documentation which follows covers use on Ubuntu 16.04. At this time, functionality on later Ubuntu releases, other Linux distributions, Windows, and Mac systems is untested. If using another operating system, please adjust instructions referencing various utilities found on the Ubuntu distribution, such as the [apt package manager](https://ubuntu.com/server/docs/package-management), to work with your environment. 

## Installation and Setup - Software Development Kits (SDKs)

### Google Assistant SDK

Note: adapted from the Google Assistant SDK guide 'Introduction to the Google Assistant Service'. Please consult the official documentation at <https://developers.google.com/assistant/sdk/guides/service/python>


#### Setup a virtual environment

In terminal (for Python 2.7 implementation):
```
sudo apt-get update
sudo apt-get install python-dev python-virtualenv
virtualenv env --no-site-packages
env/bin/python -m pip install --upgrade pip setuptools wheel
source env/bin/activate
```

#### Install Google Assistant SDK dependencies
Run the following from terminal within the activated virtual environment
```
sudo apt-get install portaudio19-dev libffi-dev libssl-dev
```

#### Install Google Assistant SDK package using pip
```
python -m pip install --upgrade google-assistant-sdk[samples]
```

### SoftBank Pynaoqi SDK

Note: adapted from the SofBank Robotics 'Python SDK - Installation Guide', which can be found at <https://developer.softbankrobotics.com/nao6/naoqi-developer-guide/sdks/python-sdk/python-sdk-installation-guide>

#### 1. Verify Python 2.7 installation

#### 2. Download NAOqi for Python
From the [NAO6 Downloads - Linux](https://developer.softbankrobotics.com/nao6/downloads/nao6-downloads-linux) page, select "Python SDK". As of writing the latest available version was pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148.  

#### 3. Extract the NAOqi SDK
In terminal or a file manager, extract the SDK from the downloaded tarball.

#### 4. Add SDK to Python path
##### From terminal:
To temporarily add Pynaoqi to the Python path, open terminal and run 
```
export PYTHONPATH=${PYTHONPATH}:/path/to/python-sdk/lib/python2.7/site-packages
``` 
The SDK will remain enabled within that terminal until the window is closed.

##### Within a script:
The Pynaoqi SDK can also be enabled from within a script to simplify the development process. The above could be accomplished in Python as follows:

```python
import sys
sys.path.append('/path/to/python-sdk/lib/python2.7/site-packages')
```
