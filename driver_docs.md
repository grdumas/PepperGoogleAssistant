# driver.sh

This bash script executes several steps of the project. 

## SSH
This command enables remote logins.
 
In this project, ssh is used to connect to the Pepper robot on a local network.

Description from the BSD General Commands Manual:
> ssh (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine. It is intended to provide secure encrypted communications between two untrusted hosts over an insecure network. X11 connections, arbitrary TCP ports and UNIX-domain sockets can also be forwarded over the secure channel.

### Basic syntax: ssh [user]@[hostname]
* *user* is the username to login as. On Pepper robot the default is 'nao'.
* *hostname* is the IP address of the Pepper robot. Pepper's IP address can be found by pressing a button on the front of the chassis, beneath the tablet. 

### Example usage
```
ssh nao@192.168.1.140
```

### Additional documentation
[SSH Unix man page](https://www2.stat.duke.edu/comp/security/ssh_man.html) from Duke University

---

## arecord
Command-line sound recorder.

Description from the BSD General Commands Manual:
> arecord is a command-line soundfile recorder for the ALSA soundcard driver. It supports several file formats and multiple soundcards with multiple devices. If recording with interleaved mode samples the file is automatically split before the 2GB filesize.

### Basic syntax: arecord [flags] [filename] 
* *filename* is the file the recording will be written to once finished. By default the file will be saved in the current directory unless specified otherwise.
* *flags* are additional options that the command can be run using. For example:
  - *-d 5* specifies that audio will be recorded for a duration of 5 seconds.
  - *-f S16_LE* specifies that the recording will be made in 16 bit little endian format.
  - *-r 16000* sets the recording to a rate of 16000 Hertz

### Example usage
```
arecord -d 5 -f S16_LE -c 1 -r 16000 -t wav query.wav
```
The parameters supplied to the “arecord” command specify that audio will be recorded for a duration of 5 seconds (-d 5), in 16 bit little endian format (-f S16_LE), at a rate of 16000 Hertz (-r 16000), and be saved to a WAV audio file with the titled query.wav once recording is complete. 

### Additional documentation
[arecord man page](https://manpages.org/arecord) from manpages.org

---

## scp
Remote file copy program. Used in driver.sh to transfer the user request from Pepper to the workstation, then to send the Google Assistant's response from the workstation to Pepper.

Description from the BSD General Commands Manual:
> scp copies files between hosts on a network. It uses ssh for data transfer, and uses the same authentication and provides the same security as ssh. scp will ask for passwords or passphrases if they are needed for authentication.

### Basic syntax: scp [[user@]host1:]file1 ... [[user@]host1:]file2
* *user@host1* takes the username and IP address or hostname of the system the file is to be copied from.  
* *file1* is the original file you want to copy.
* *user@host2* takes the username and IP address or hostname of the system the file is to be copied to. 
* *file2* is the copied file that will be created.

### Example usage
```
scp /home/user/env/test/syn.wav nao@192.168.1.140:/home/nao
```
Copies a file, syn.wav, from the specified directory (filepath starts at /home) to the directory 'nao' on a Pepper robot with IP address 192.168.1.140.

### Additional documentation
[scp man page](https://manpages.org/scp) from manpages.org