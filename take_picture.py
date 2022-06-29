# import all lib required
import datetime
import shutil
import picamera


def take_picture(width: int, height: int, pictureType: str):
    # create camera object and defined his resolution
    camera = picamera.PiCamera()
    camera.resolution = (width, height)

    # try finally to create a picture with a specified name and move it at a specified place
    try:
        # create the name of the picture
        date = datetime.datetime.now()
        fileName = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '_T' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second) + '-' + str(date.microsecond)[:-3] + '_M' + pictureType + '.jpeg'

        # take the picture
        camera.capture(fileName, 'jpeg')

        # move the picture
        file_source = '/home/admin/Desktop/script/' + fileName
        file_destination = '/home/admin/Images/security/' + fileName
        shutil.move(file_source, file_destination)
    finally:
        # close connection with the camera
        camera.close()
