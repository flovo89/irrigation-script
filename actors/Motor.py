import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    def setState(self, on):
        self.state = on
        GPIO.output(self.pin, on)

    def getState(self):
        return self.state
