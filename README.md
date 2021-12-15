# LegoBoostCmdPy
Python program to control Lego Boost with input commands or file.

# Getting Started
1. download/clone the respository. These steps assume that the code is under /home/pi/LegoBoostCmdPy.
2. Install dependencies. 
   * install IotDevicesPy at https://github.com/rphuang/IotDevicesPy
   * install flask (for video streaming)
3. Run command with sample file.

# Examples
1. run sample command file on Windows
   * run the code
```
cd LegoBoostCmdPy
py boostCmd.py
```
   * After the prompt, type "start" and then power on the boost.
   * type "run sampleCmd.txt" to run the commands in the file.
   * type "shutoff" to turn off the boost
   * type "end" to exit
2. run sample command file on Raspberry Pi with camera. You can attach the Pi to Boost.
   * run the code (need to use sudo)
```
cd LegoBoostCmdPy
sudo py boostCmd-picam.py
```
   * launch browser to http://localhost:8000 to view the streaming video
   * After the prompt, type "start" and then power on the boost.
   * type "run sampleCmd.txt" to run the commands in the file.
   * type "shutoff" to turn off the boost
   * type "end" to exit
![Boost Vernie with RasPi](https://github.com/rphuang/IotDevicesPy/examples/VernieRasPi.jpg)


