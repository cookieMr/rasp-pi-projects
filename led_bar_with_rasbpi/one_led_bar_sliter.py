import RPi.GPIO as GPIO
import time

cathodes = [11, 13, 15, 19]
anodes = [38, 40]

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

for cathode in cathodes:
    GPIO.setup(cathode, GPIO.OUT)
    GPIO.output(cathode, GPIO.LOW)

for anode in anodes:
    GPIO.setup(anode, GPIO.OUT)
    GPIO.output(anode, GPIO.LOW)

counter = 10

try:
    while (counter > 0):
        counter -= 1

        for anode in anodes:
            GPIO.output(anode, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(anode, GPIO.LOW)

finally:
    GPIO.cleanup()
