from IotLib.config import Config
from CameraLib.cameraPi import Camera
from boostCmd import BoostCmd
from streamingService import startVideoStreamAsync

# load both boost and video settings
config = Config('boostconfig.txt', autoSave=False)
config.addSettings('videoconfig-pi.txt')

# create camera
camera = Camera.createCamera(config)

# start video streaming in separate thread
startVideoStreamAsync(camera, config, debug=True)

# run boostCmd
cmd = BoostCmd(config, camera)
cmd.run()

