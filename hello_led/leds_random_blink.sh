#!/bin/bash

RED_PIN=14
YELLOW_PIN=24
BLUE_PIN=18
GREEN_PIN=23

ALL_PINS=($RED_PIN $YELLOW_PIN $BLUE_PIN $GREEN_PIN)
PINS_STATUS=(0 0 0 0)

SLEEP_DURATION=0.1

led_on () {
	raspi-gpio set $1 dh
	sleep $SLEEP_DURATION
}

led_off () {
	raspi-gpio set "$1" dl
	sleep $SLEEP_DURATION
}

get_all_pins_info () {
	for pin in ${ALL_PINS[@]}; do
		raspi-gpio get $pin
	done
}

reset_all_pins () {
	for pin in ${ALL_PINS[@]}; do
		# TODO: pull down
		raspi-gpio set $pin ip dl &>/dev/null
	done
}

init_all_pins () {
	for pin in ${ALL_PINS[@]}; do
		raspi-gpio set $pin op &>/dev/null
	done
}

get_all_pins_info
init_all_pins

for i in {1..100}; do
	INDEX=$(( $RANDOM % 4 ))
	THE_PIN=${ALL_PINS[$INDEX]}
	STATUS=${PINS_STATUS[$INDEX]}

	if [ "$STATUS" -eq "0" ]; then
		PINS_STATUS[$INDEX]=1
		led_on $THE_PIN
	else
		PINS_STATUS[$INDEX]=0
		led_off $THE_PIN
	fi
done

reset_all_pins
get_all_pins_info

