import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def getState(self):
        return GPIO.input(self.pin)