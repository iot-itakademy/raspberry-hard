import threading
import RPi.GPIO as GPIO
import time
import json
from take_picture import take_picture
from urllib import request
import requests


# minimumDistance = requests.get('https://').json()

try:
    # setup motion sensore
    GPIO.setmode(GPIO.BCM)

    try:
        with request.urlopen("http://www.scrutoscope.live/api/settings") as url:
            data = json.loads(url.read().decode())
    except:
        print('error')

    Trig = 23
    Echo = 24
    amountPicture = data[0]['amountCapture']

    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

    GPIO.output(Trig, False)

    previous = 0
    callApi = 0
    while True:
        if callApi == 0:
            try:
                with request.urlopen("http://www.scrutoscope.live/api/settings/camera/1") as url:
                    data = json.loads(url.read().decode())
            except:
                print('error')
            minimumDistance = json.loads((data[0]['params']))['distance']
            width = json.loads((data[0]['params']))['width']
            height = json.loads((data[0]['params']))['height']
            pictureType = data[0]['type']['type']
            callApi = 20
        else:
            callApi = callApi - 1

        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)
        while GPIO.input(Echo) == 0:  # send ultrasound
            startImpulse = time.time()

        while GPIO.input(Echo) == 1:  # return of the echo
            endImpulse = time.time()

        distance = int(round((endImpulse - startImpulse) * 340 * 100 / 2, 1))  # calculate distance (cm)
        print('distance: ' + str(distance),'previous: ' + str(previous),'minimumDistance: ' + str(minimumDistance))
        # if the new distance is less than the previous or if the new distance is less than 2 meters it takes a picture
        if distance <= minimumDistance and previous <= minimumDistance:
            print('"click"')
            threads = [threading.Thread(target=take_picture(width, height, pictureType)) for _ in range(amountPicture)]
            [thread.start() for thread in threads]
            [thread.join() for thread in threads]

            url = 'http://www.scrutoscope.live/api/Statistics/post'
            data = {"amount": amountPicture, "type": pictureType}

            req = requests.post(url, json=data)

        previous = distance
finally:
    GPIO.cleanup()
