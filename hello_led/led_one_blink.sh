#!/bin/bash

GPIO_PIN=14
SLEEP_DURATION=0.3

led_on () {
	raspi-gpio set $GPIO_PIN dh
	sleep $SLEEP_DURATION
}

led_off () {
	raspi-gpio set $GPIO_PIN dl
	sleep $SLEEP_DURATION
}

raspi-gpio get $GPIO_PIN

raspi-gpio set $GPIO_PIN op &>/dev/null
for i in {1..2000}; do
	led_on
	led_off
done

raspi-gpio set $GPIO_PIN ip dl &>/dev/null
raspi-gpio get $GPIO_PIN

