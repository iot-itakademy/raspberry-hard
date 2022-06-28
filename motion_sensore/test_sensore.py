import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BCM)

    Trig = 23  # Entree Trig du HC-SR04 branchee au GPIO 23
    Echo = 24  # Sortie Echo du HC-SR04 branchee au GPIO 24

    GPIO.setup(Trig, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

    GPIO.output(Trig, False)

    previous = 0
    while True:
        time.sleep(1)  # On la prend toute les 1 seconde
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:  # Emission de l'ultrason
            startImpulse = time.time()

        while GPIO.input(Echo) == 1:  # Retour de l'Echo
            endImpulse = time.time()

        distance = round((endImpulse - startImpulse) * 340 * 100 / 2, 1)  # Vitesse du son = 340 m/s

        if distance < previous | (distance - previous) < 5:
            print(distance, previous)
finally:
    GPIO.cleanup()
