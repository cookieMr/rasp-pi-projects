# Hello LED Scripts

Each script can be run with the same breadboard configuration with
all 4 LEDs connected (even if script toggles just 1 LED).

## Breadboard

The GPIO numbering is quite different than the pin numbering on a Raspberry Pi physical board. In the following schematic LEDs are connected as described in the table.

For more info on GPIO/Raspberry physical board numbering see [this webpage](https://pinout.xyz/).

| LED color | GPIO | Breadboard |
|-----------|------|------------|
| red       | 14   |  8         |
| yellow    | 18   | 12         |
| blue      | 23   | 16         |
| green     | 24   | 18         |

The ground pin on a Raspberry physical board is 6.

---

### LED resistors

Each LED requires a resistor. See the following equasion. Symbols are described
in a table.

```
R = (Vp - Vd) / Id
```

| Symbol | Unit  |  Description   |
|--------|-------|----------------|
| R      | Ohm   | Resistor value |
| Vp     | Volt  | Power voltage  |
| Vd     | Volt  | LED voltage    |
| Id     | Amper | LED current    |

* `Vp` a power voltage needs to be greater than `Vd` (we need to provide more voltage than LED can consume), otherwise LED won't light up
* each GPIO outputs `5V`
* `Id` for each LED is the same `0.007A` (which can be represented as `7mA`).
* red LED `Vd` is between `1.6V` and `2.2V`; we take average `1.9V`
* yellow LED `Vd` is between `2V` and `2.3V`; we take average `2.1V`
* blue LED `Vd` is between `2V` and `3.7V`; we take average `3.5V`
* green LED `Vd` is between `2.9V` and `4V`; we take average `2.8V`

After calculating with already presented equasion we get:
 * red's resister 443 Ohm; closest value is 470 Ohm 
 * yellow's resister 414 Ohm; closest value is 470 Ohm
 * blue's resister 214 Ohm; closest value is 220 Ohm
 * green's resister 314 Ohm; closest value is 320 Ohm (thus two resistors 220 + 100) Ohm

[![Created with Circut Diagram Webpage](circuit.png)](https://www.circuit-diagram.org/)

---

## Bash

Raspberry OS comes with preinstalled `raspi-gpio` CLI tool.

Running `raspi-gpio set 14 op dh` will light up LED connected to GPIO 14 (in this case red LED).

Running `raspi-gpio set 14 dl` will turn it off.

There are 3 bash scripts that run these commands:
 * `./led_one_blink.sh`
 * `./leds_four_blink.sh`
 * `./leds_random_blink.sh`

---

## Python

Use Virtual Environemnts to not mess up with localy installed Python.
1. Create venv with `python3  -m venv ./venv` command
1. Activate it by running `source ./venv/bin/activate`
1. Install a python module for RPi GPIO `pip install RPi.GPIO`
1. Run one of the scripts:
 * `python led_one_blink.py`
 * `python leds_four_blink.py`
 * `python leds_random_blink.py`
1. Deactivate venv `deactivate`
