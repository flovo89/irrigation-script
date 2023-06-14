from actors.Motor import Motor
from sensors.Sensor import Sensor
import time

pumpIn = Motor(1)
pumpOut = Motor(2)
sensorFull = Sensor(3)
sensorEmpty = Sensor(4)

def isFull():
    return sensorFull.getState()

def isEmpty():
    return sensorEmpty.getState()

def pumpWater(fill, maxtime_s = 120):
    count = 0
    ret = False
    if fill:
        pumpOut.setState(True)
    else:
        pumpIn.setState(True)

    while count < maxtime_s:
        count = count + 1
        if fill:
            if isFull():
                ret = True
                break
        else:
            if isEmpty():
                ret = True
                break
        time.sleep(1)

    pumpIn.setState(False)
    pumpOut.setState(False)
    return ret



#########################################################
# Main flow
#########################################################
if not pumpWater(True, 60):
    raise Exception("Could not fill tank")

time.sleep(60)

if not pumpWater(False, 60):
    raise Exception("Could not empty tank")

