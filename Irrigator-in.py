import RPi.GPIO as GPIO
from actors.Motor import Motor
from sensors.Sensor import Sensor
import time

pumpInA = Motor(2)
pumpInB = Motor(3)
sensorEmpty = Sensor(21)

def isEmpty():
    return sensorEmpty.getState()

def pumpWater(motor, time_s):
    count = 0
    motor.setState(True)

    while count < time_s:
        count = count + 1
        if isEmpty():
            break
        time.sleep(1)

    motor.setState(False)


#########################################################
# Main flow
#########################################################
pumpWater(pumpInA, 15)
pumpWater(pumpInB, 15)

GPIO.cleanup()

