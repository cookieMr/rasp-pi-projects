# Hello LED
This project runs a simple python app to play with LED connected
to a Raspberry Pi.

## Python Venv (Virtual Env)
1. Create venv with `python3  -m venv ./venv` command.
1. Activate it by running `source ./venv/bin/activate`.
1. Use `pip` to intall all the needed libraries.
    * Actually use the `requirements.txt` file to install libraries that were chosen for this project. Execute the following command *after* venv was activated.
    ```bash
    pip install -r requirements.txt
    ```
1. Deactivate it by running just `deactivate`.
1. Optionally, after dactivating venv you can remote it with `rm -r ./venv`.

Watch [this Youtube](https://www.youtube.com/watch?v=KxvKCSwlUv8)
video for details about Python' Virtual Environments.

## Running Script
It's as simple as this:
```bash
python hello_led.py
```