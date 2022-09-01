import RPi.GPIO as GPIO
import time
from random import randint

red_led = 14
yellow_led = 24
blue_led = 18
green_led = 23

all_leds = [red_led, yellow_led, blue_led, green_led]
leds_status = [False, False, False, False]

def ledOn(pinNr: int):
    GPIO.output(pinNr, GPIO.HIGH)
    time.sleep(.2)

def ledOff(pinNr: int):
    GPIO.output(pinNr, GPIO.LOW)
    time.sleep(.2)


GPIO.setmode(GPIO.BCM)
for led in all_leds:
    GPIO.setup(led, GPIO.OUT)

for i in range(50):
    index = randint(0, len(all_leds)) - 1
    the_led_pin = all_leds[index]
    the_led_status = leds_status[index]

    if (the_led_status):
        leds_status[index] = False
        ledOff(the_led_pin)
    else:
        leds_status[index] = True
        ledOn(the_led_pin)

for led in all_leds:
    ledOff(led)

GPIO.cleanup()

