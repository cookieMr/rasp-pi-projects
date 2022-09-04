import RPi.GPIO as GPIO
import time

button1_pin = 16
button2_pin = 18

red_led_pin = 7
yellow_led_pin = 11
blue_led_pin = 13
green_led_pin = 37
white_led_pin = 15
all_led_pins = [red_led_pin, yellow_led_pin, blue_led_pin, green_led_pin, white_led_pin]

def all_led_on():
    for led_pin in all_led_pins:
        GPIO.output(led_pin, GPIO.HIGH)

def all_led_off():
    for led_pin in all_led_pins:
        GPIO.output(led_pin, GPIO.LOW)

def setup_all():
    GPIO.setmode(GPIO.BOARD)

    for led_pin in all_led_pins:
        GPIO.setup(led_pin, GPIO.OUT)
    all_led_off()
    
    for button_pin in [button1_pin, button2_pin]:
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# This GPIO mode takes in the physical pin numbers as an input
setup_all()

while True:
    if GPIO.input(button1_pin) == GPIO.LOW:
        all_led_on()
    if GPIO.input(button2_pin) == GPIO.LOW:
        all_led_off()
    time.sleep(.2)

