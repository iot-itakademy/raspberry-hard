import datetime
import os
import shutil
import time
import libcamera

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

try:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    date = datetime.datetime.now()
    fileName = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '_T' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second) + '_MManual.jpg'
    resize = (2592, 1944)
    camera.capture(fileName, 'jpg', None, False, resize)
    file_source = '/home/admin/Desktop/script/' + fileName
    file_destination = '/home/admin/Images/security' + fileName

    shutil.move(file_source, file_destination)

finally:
    camera.close()
