# Controlling LED with a Button

## Python

Use Virtual Environemnts to not mess up with localy installed Python.
1. Create venv with `python -m venv ./venv` command
1. Activate it by running `source ./venv/bin/activate`
1. Install a python module for RPi GPIO `pip install gpiozero`
1. Run one of the scripts:
   * `python led_with_button.py`
1. Deactivate venv `deactivate`