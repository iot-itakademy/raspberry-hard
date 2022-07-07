import threading
import RPi.GPIO as GPIO
import time
import json
from take_picture import take_picture
from urllib import request
import requests


try:
    # setup motion sensore
    GPIO.setmode(GPIO.BCM)

    # get some params from the API
    try:
        with request.urlopen("http://www.scrutoscope.live/api/settings") as url:
            data = json.loads(url.read().decode())
    except:
        print('error')

    Trig = 23
    Echo = 24
    previous = 0
    callApi = 0
    amountPicture = data[0]['amountCapture']

    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)
    GPIO.output(Trig, False)

    # main code loop
    while True:
        # if there is no call to the API we call the API (every 20 loop it calls the API)
        if callApi == 0:
            try:
                with request.urlopen("http://www.scrutoscope.live/api/settings/camera/1") as url:
                    data = json.loads(url.read().decode())
            except:
                print('error')
                exit()

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

        # if the new distance is less than the previous or if the new distance is less than 2 meters it takes a picture
        if distance <= minimumDistance and previous <= minimumDistance:
            # take amount of picture defined by the API
            threads = [threading.Thread(target=take_picture(width, height, pictureType)) for _ in range(amountPicture)]
            [thread.start() for thread in threads]
            [thread.join() for thread in threads]

            # send the fact that we take some pictures for statistics
            url = 'http://www.scrutoscope.live/api/Statistics/post'
            data = {"amount": amountPicture, "type": pictureType}
            req = requests.post(url, json=data)

        previous = distance
finally:
    GPIO.cleanup()
