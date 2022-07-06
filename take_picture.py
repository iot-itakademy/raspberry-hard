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
        month = str(date.month)
        day = str(date.day)
        hour = str(date.hour)
        minute = str(date.minute)
        second = str(date.second)
        microsecond = str(date.microsecond)[:-3]

        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
        if len(hour) < 2:
            hour = '0' + hour
        if len(minute) < 2:
            minute = '0' + minute
        if len(second) < 2:
            second = '0' + second
        if len(microsecond) < 3:
            microsecond = '0' + microsecond

        fileName = str(date.year) + '-' + month + '-' + day + '-' + hour + '-' + minute + '-' + second + '-' + microsecond + '_M' + pictureType + '.jpeg'

        # take the picture
        camera.capture(fileName, 'jpeg')

        # move the picture
        file_source = '/home/admin/Desktop/script/' + fileName
        file_destination = '/home/admin/Images/security/' + fileName
        shutil.move(file_source, file_destination)
    finally:
        # close connection with the camera
        camera.close()
