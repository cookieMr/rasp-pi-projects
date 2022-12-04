import RPi.GPIO as GPIO
import time

cathodes = [11, 13, 15, 19]
anodes = [38, 40]
counter = 10

leds = [
    [anodes[0], cathodes[11]],
    [anodes[0], cathodes[13]],
    [anodes[0], cathodes[15]],
    [anodes[0], cathodes[19]],
    [anodes[1], cathodes[11]],
    [anodes[1], cathodes[13]],
    [anodes[1], cathodes[15]],
    [anodes[1], cathodes[19]]
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

def turn_on_one_led(the_anode: Int, the_cathode: Int):
    for anode in anodes:
        GPIO.output(anode, GPIO.LOW if anode != the_anode else GPIO.HIGH)
    for cathode in cathodes:
        GPIO.output(anode, GPIO.HIGH if cathode != the_cathode else GPIO.LOW)

def turn_all_off():
    for anode in anodes:
        GPIO.output(anode, GPIO.LOW)
    for cathode in cathodes:
        GPIO.output(anode, GPIO.LOW)

try:
    setup()
    while (counter > 0):
        for led in leds:
            turn_on_one_led(led[0], led[1])
            time.sleep(0.1)
            turn_all_off()

except KeyboardInterrupt:
    turn_all_off()

finally:
    GPIO.cleanup()
