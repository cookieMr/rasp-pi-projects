import RPi.GPIO as GPIO
import time

red_led = 14
yellow_led = 24
blue_led = 18
green_led = 23

all_leds = [red_led, yellow_led, blue_led, green_led]

def ledOn(pinNr: int):
    GPIO.output(pinNr, GPIO.HIGH)
    time.sleep(.2)

def ledOff(pinNr: int):
    GPIO.output(pinNr, GPIO.LOW)
    time.sleep(.2)


GPIO.setmode(GPIO.BCM)
for led in all_leds:
    GPIO.setup(led, GPIO.OUT)

for i in range(10):
    for led in all_leds:
        ledOn(led)
    for led in all_leds:
        ledOff(led)

GPIO.cleanup()

