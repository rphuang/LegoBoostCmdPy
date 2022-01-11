# LegoBoostCmdPy
Python program to control Lego Boost with input commands or file.

# Getting Started
1. download/clone the respository. These steps assume that the code is under /home/pi/LegoBoostCmdPy.
2. Install dependencies. 
   * install IotDevicesPy at https://github.com/rphuang/IotDevicesPy
   * install flask (for video streaming)
3. Run command with sample file.
	1. run sample command file on Windows
	   * run the code: py boostCmd.py
	   * After the prompt, type "start" and then power on the boost.
	   * type "run sampleCmd.txt" to run the commands in the file.
	   * type "shutoff" to turn off the boost
	   * type "end" to exit
	2. run sample command file on Raspberry Pi with camera. You can attach the Pi to Boost.
	   * run the code: sudo python3 boostCmd-picam.py
	   * launch browser to http://localhost:8000 to view the streaming video
	   * After the prompt, type "start" and then power on the boost.
	   * type "run sampleCmd.txt" to run the commands in the file.
	   * type "shutoff" to turn off the boost
	   * type "end" to exit

# Distance Checker
One of the feature is to stop Boost when it runs to obstacle using the distance sensor. This is by running a distance checker in separate thread. When enabled, the distance checker will slow down the Boost bot and stop it based on the configuration settings.

# Auto Modes
The command supports several auto modes:
1. Wander (mode wander) - when enabled, the prog uses the distance sensor to control Boost to wander around. It runs backward when encounters an obstacle the try to find an open route to continue. The followings are the primary states for the wander mode.
	* Moving - move forward until it is stopped by sensing obstacle
	* Backward - move backward when encounter obstacle
	* Scan - move Boost to different direction and try to find an open route to move. It starts moving once an open route is found.
2. Follow (mode follow) - set to this mode allows Boost to follow an object detected by the distance sensor. Note that, for now, this mode only supports forward/backward movements (no turning).
3. Face tracking (mode face) - this is only available when running on Raspberry Pi with camera.
4. Manual (mode manual) - use manual mode to turn off any of the above auto modes.

# Configuration
* Boost Configuration - boostconfig.txt
    * motor speed & power
		* motor.minMovingSpeed - min speed for all motors
		* motor.maxPower - max power for all motors
	* distance checker configuration
		* distanceChecker.enableThread - set to 1 to enable distance checking
		* distanceChecker.scanCycleInSecond - specify how often to run the distance check
		* distanceChecker.stopDistance - the distance to stop (in meter)
		* distanceChecker.emergencyStopDistance - the distance to emergency stop (in meter)
		* distanceChecker.slowdownDistance - the distance to slowdown (in meter)
		* distanceChecker.maxSlowdownSpeed - the max slowdown speed during distance check
	* auto modes configuration
		* auto.defaultSpeed - the default speed for auto modes
		* auto.forwardSpeed - the forward speed for auto modes
		* auto.backwardSpeed - the backward speed for auto modes
		* wander.backwardTime - number of seconds to move backward in wander mode when in front of obstacle
		* wander.stateTimeout - timeout in seconds for all states in wander mode
		* wander.stateDelayInSecond - delay between states in wander mode
		* follow.maxFollowDistance - the maximum distance to follow in meter (9 inch is the sensor limit)
		* follow.distanceOffset - controls the sensitivity for follow mode
		* follow.followDistance - the distance in meter for Boost to follow the object
		* follow.slowdownDistance - the distance to slowdown in follow mode (in meter)
* Video Configuration - videoconfig-pi.txt
	* camera.width - camera width resolution
	* camera.height - camera height resolution
	* camera.drawCrosshair - whether to draw crosshair
	* video.httpVideoPort - the HTTP port number for streaming video
	* video.enableFaceTracking - whether to enable face tracking or not
	* video.classifier - the xml file for face tracking classifier
	* video.indexHtml - the index html file for video streaming

