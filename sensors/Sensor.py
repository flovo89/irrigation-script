import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)

    def getState(self):
        return GPIO.input(self.pin)