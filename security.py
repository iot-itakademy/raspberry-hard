import RPi.GPIO as GPIO
import time
from take_picture import take_picture
import urllib.request, json

# minimumDistance = requests.get('https://').json()

try:
    # setup motion sensore
    GPIO.setmode(GPIO.BCM)

    Trig = 23
    Echo = 24

    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

    GPIO.output(Trig, False)

    previous = 0
    callApi = 0
    while True:
        if callApi == 0:
            with urllib.request.urlopen("http://www.scrutoscope.live/api/settings/camera/1") as url:
                data = json.loads(url.read().decode())

            minimumDistance = json.loads((data[0]['params']))['distance']
            width = json.loads((data[0]['params']))['width']
            height = json.loads((data[0]['params']))['height']
            pictureType = data[0]['type']['type']
            callApi = 20
        else:
            callApi = callApi - 1

        # time.sleep(1)  # each seconds
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:  # send ultrasound
            startImpulse = time.time()

        while GPIO.input(Echo) == 1:  # return of the echo
            endImpulse = time.time()

        distance = int(round((endImpulse - startImpulse) * 340 * 100 / 2, 1))  # calculate distance (cm)
        print('distance: ' + str(distance), 'previous: ' + str(previous))

        # if the new distance is less than the previous or if the new distance is less than 2 meters it takes a picture
        if (distance < previous and distance <= 10) or distance <= minimumDistance:
            take_picture(width, height, pictureType)

        previous = distance
finally:
    GPIO.cleanup()
