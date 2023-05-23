# Galactic Unicorn Project

A project to display useful information on Pico display boards.

## Installation

Install the non-screen specific version of the pico-w [micropython firmware](pimoroni-picow-v1.20.2-micropython.uf2).

Clone the repo:
```bash
git clone https://github.com/DaveTrainor/galactic-unicorn-project.git
cd galactic-unicorn-project
pip install -r requirements.txt
```

Make changes to or create the `settings.py` file depending on your usage.

```python
screen = {
    'driver': 'pico_unicorn',
    # 'driver': ''galactic_unicorn'
}
network = {
    'driver': 'pico_w',
    'ssid': '<wifi network name>',
    'password': '<wifi network password>',
}

locale = {
    'coordinates': (0.00, 0.00), #replace with lattitude / longitude values (Google maps)
    'timezone': 'Europe/London', #replace with correct zone from https://worldtimeapi.org/api/timezone/
}
```

## Deploy

```bash
pico-up push
```
## Debug

* run `mpremote devs` to get your device address. E.g. `/dev/cu.usbmodem2101`
* `mpremote connect [put address here]`  then `ctrl D` to see outputs in the terminal
* `ctrl ]` to exit

