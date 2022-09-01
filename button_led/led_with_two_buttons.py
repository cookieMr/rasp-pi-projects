import RPi.GPIO as GPIO
import time

button1_pin = 16
button2_pin = 18
red_led_pin = 7

# This GPIO mode takes in the physical pin numbers as an input
GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(button1_pin) == GPIO.LOW:
        GPIO.output(red_led_pin, GPIO.LOW)
    if GPIO.input(button2_pin) == GPIO.LOW:
        GPIO.output(red_led_pin, GPIO.HIGH)
    time.sleep(.2)

