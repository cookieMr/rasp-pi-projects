import PRi.GPIO as GPIO
import time

cathodes = [11, 13, 15, 19]
anodes = [38, 40]



for cathode in cathods:
    GPIO.setup(cathode, GPIO.OUT)
    GPIO.output(cathode, 0)

for anode in anodes:
    GPIO.setup(anode, GPIO.OUT)
    GPIO.output(anode, 0)

try:
    while True:
        for c in cathods:
            GPIO.output(c, 1)
            time.sleep(0.3)
            GPIO.output(c, 0)
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()

