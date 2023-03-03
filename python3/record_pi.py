from datetime import datetime, timedelta
import picamera
import shutil
import os

os.chdir("/home/pi/Pictures")

camera = picamera.PiCamera()
#camera.resolution = (640, 480)
#camera.framerate = 12 
camera.stop_preview()
for x in range(0, 3):
	total, used, free = shutil.disk_usage("/")
	print('free space', (free // (2**20)), '  at', str(datetime.now()))
	if ((free // (2**20)) > 300):
		s = str(datetime.now())
		s=s.replace(':','.')
		s=s.replace(' ','.')
		camera.start_recording('video'+s+'.h264', quality=30)
		camera.wait_recording(60)
		camera.stop_recording()
