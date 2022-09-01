import RPi.GPIO as GPIO
import time

led = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.2)

GPIO.cleanup()

