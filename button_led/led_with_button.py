from gpiozero import LED, Button        

led = LED(4)
button = Button(17)

while True:
        button.wait_for_press()
        led.on()

        button.wait_for_release()
        led.off()
