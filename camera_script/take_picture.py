import datetime
import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)
try:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('foo.jpg')
    print(datetime.datetime)
finally:
    camera.close()
