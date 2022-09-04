# Controlling LED with a Potenciometer

## Breadboard

The breadbord schematic will use the BCM mode (just like the python script).

Raspberry Pi rads the GPIO pin as one of two values `0` and `1`. So the
potenciometer needs to be turn on completly (all the way) to be read as `1`.
Otherwise it'll be read as `0` even it the potenciometer is half way turned.

## Python

Use Virtual Environemnts to not mess up with localy installed Python.

1. Create venv with `python -m venv ./venv` command
1. Activate it by running `source ./venv/bin/activate`
1. Install two python modules for RPi GPIO via a `requirements.txt` file:
   * `pip install -r requirements.txt`
1. Run one of the scripts:
   * `python led_with_potenciometer.py`
1. Deactivate venv `deactivate`

