import RPi.GPIO as GPIO
import time
import take_picture

try:
    # setup motion sensore
    GPIO.setmode(GPIO.BCM)

    Trig = 23
    Echo = 24

    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

    GPIO.output(Trig, False)

    previous = 0
    while True:
        time.sleep(1)  # each seconds
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:  # send ultrasound
            startImpulse = time.time()

        while GPIO.input(Echo) == 1:  # return of the echo
            endImpulse = time.time()

        distance = round((endImpulse - startImpulse) * 340 * 100 / 2, 1)  # calculate distance (cm)

        # if the new distance is less than the previous or if the new distance is less than 2 meters it takes a picture
        if distance < previous | distance <= 200:
            take_picture.take_picture()
finally:
    GPIO.cleanup()
