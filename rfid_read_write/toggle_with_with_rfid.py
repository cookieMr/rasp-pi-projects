import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

led_pin = 16
turn_on_cmd = 'Turn LED on!'
turn_off_cmd = 'Turn LED off!'

def turn_led_on():
    GPIO.output(led_pin, GPIO.HIGH)

def turn_led_off():
    GPIO.output(led_pin, GPIO.LOW)

def setup() -> SimpleMFRC522:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    return SimpleMFRC522()

try:
    reader = setup()
    while True:
        id, text = reader.read()
        text = text.strip()

        print(text)
        if (text == turn_on_cmd):
            turn_led_on()
        elif (text == turn_off_cmd):
            turn_led_off()
        else:
            print('Unknown command!')
        time.sleep(0.2)
finally:
    GPIO.cleanup()

