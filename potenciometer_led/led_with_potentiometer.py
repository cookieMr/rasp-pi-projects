import RPi.GPIO as gpio
import time

led_pin = 12
potentiometer_pin = 14

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)
gpio.setup(potentiometer_pin, gpio.IN)
gpio.output(led_pin, gpio.LOW)

while True:
    if (gpio.input(potentiometer_pin) == gpio.HIGH):
        print("Potentiometer is in ON state.")
        gpio.output(led_pin, gpio.LOW)
    else:
        print("Potentiometer is in OFF state.")
        gpio.output(led_pin, gpio.HIGH)
    time.sleep(.2)

gpio.cleanup()
