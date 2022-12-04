import RPi.GPIO as GPIO
import time

cathodes = [11, 13, 15, 19]
anodes = [38, 40]
counter = 1

leds = [
    [anodes[0], cathodes[0]],
    [anodes[0], cathodes[1]],
    [anodes[0], cathodes[2]],
    [anodes[0], cathodes[3]],
    [anodes[1], cathodes[0]],
    [anodes[1], cathodes[1]],
    [anodes[1], cathodes[2]],
    [anodes[1], cathodes[3]]
    ]

def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)

    for cathode in cathodes:
        GPIO.setup(cathode, GPIO.OUT)
        GPIO.output(cathode, GPIO.LOW)

    for anode in anodes:
        GPIO.setup(anode, GPIO.OUT)
        GPIO.output(anode, GPIO.LOW)

def turn_on_one_led(the_anode: int, the_cathode: int):
    for anode in anodes:
        GPIO.output(anode, GPIO.HIGH if anode == the_anode else GPIO.LOW)
    for cathode in cathodes:
        GPIO.output(anode, GPIO.LOW if cathode == the_cathode else GPIO.HIGH)

def turn_off_all():
    for anode in anodes:
        GPIO.output(anode, GPIO.LOW)
    for cathode in cathodes:
        GPIO.output(anode, GPIO.HIGH)

try:
    setup()
    
    for led in leds:
        turn_on_one_led(led[0], led[1])
        time.sleep(0.1)
    
    time.sleep(0.1)
except KeyboardInterrupt:
    turn_off_all()

finally:
    GPIO.cleanup()
