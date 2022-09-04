import RPi.GPIO as GPIO
import time

button_pin = 16
led_pin = 7

def ledOn(pin: int):
    GPIO.output(pin, GPIO.HIGH)

def ledOff(pin: int):
    GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(button_pin):
        ledOff(led_pin)
    else:
        ledOn(led_pin)
    time.sleep(.2)

