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
wifi = {
    'driver': 'pico_w',
    'ssid': '<wifi network name>',
    'password': '<wifi network password>',
}
```

## Deploy

```bash
pico-up push
```
