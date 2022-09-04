import RPi.GPIO as gpio
import time

led_pin = 12
potenciometer_pin = 14

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)
gpio.setup(potenciometer_pin, gpio.IN)
gpio.output(led_pin, gpio.LOW)

while True:
    if (gpio.input(potenciometer_pin) == gpio.HIGH):
        print("Potenciometer is in ON state.")
        gpio.output(led_pin, gpio.LOW)
    else:
        print("Potenciometer is in OFF state.")
        gpio.output(led_pin, gpio.HIGH)
    time.sleep(.2)

gpio.cleanup()
