# Galactic Unicorn Project

A project to display useful information on Pico display boards.

## Installation

```bash
git clone https://github.com/DaveTrainor/galactic-unicorn-project.git
cd galactic-unicorn-project
pip install -r requirements.txt
```

Make changes to or create the `settings.py` file depending on your usage.

```python
screen = {
    'driver': 'pico_unicorn',
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
