# Galactic Unicorn Project 🦄🌟

A project to display useful information on Pico display boards.

---

## Getting Started

### Hardware Requirements

The project is based on using a Raspberry Pi Pico-W microncontroller with a supported RGB LED matrix display. The two variants of this that we have used are:
1) [Galactic Unicorn](https://shop.pimoroni.com/products/galactic-unicorn?variant=40057440960595)

    Comes with Pico-W microncontroller already onboard. 

 or

2)  Pico Unicorn.

    This doesn't have a Pico-W onboard, so you need to buy it seperately:
    - Pico-W microcontroller.
      - Can be purcased [with](https://shop.pimoroni.com/products/raspberry-pi-pico-w?variant=40454061752403) or [without](https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227) headers. Get the pre-headed version if you don't want to solder them on yourself!
    - The [The Pico Unicorn Pack Display Module](https://shop.pimoroni.com/products/pico-unicorn-pack?variant=32369501306963).


### New to Pico microcontrollers?

- [This guide](https://learn.pimoroni.com/article/getting-started-with-pico) covers the basics of using a Pico microcontroller.
- [This repo](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_unicorn) contains some demo programs for the Unicorn Pack.

---

## Installation

- Install the non-screen specific version of the pico-w [micropython firmware](https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md) (eg. pimoroni-picow-v1.20.2-micropython.uf2).

- Clone the repo:
```bash
git clone https://github.com/DaveTrainor/galactic-unicorn-project.git
cd galactic-unicorn-project
```

- Create a virtual Python environment in the project's root directory.  
[This guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) explains how & why.

- Install project dependencies:
```bash
pip install -r requirements.txt
```

- Make changes to or create the `settings.py` (depending on your usage) in the root directory:

```python
screen = {
    'driver': 'pico_unicorn',
    # 'driver': 'galactic_unicorn'
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

- Connect to the Pico:  
  
  Get your device address (eg. `/dev/cu.usbmodem2101`):
  
  
  ```bash
  mpremote devs
  ``` 

   Connect to the Pico:
  ```bash
  mpremote connect [put address here]
  ```

  `ctrl ]` to exit.
- Deploy to the Pico 👇

---

## Deployment

- Deploy to the Pico:

  ```bash
  pico-up push
  ```

- After deployment the display should show the following patterns:

  |Pattern|Meaning|
  |-|-|
  |Green Column|The screen is connected.|
  |Green Column + Flashing Blue Column| Connecting to WiFi.|
  |4 Green Flashes| WiFi connected. This pattern shows very briefly, then the display shows one of the installed programs.|

- These patterns indicate an error:

  |Pattern|Meaning|
  |-|-|
  |Red Column|Device failed to set up properly.|
  |Red LEDs in each corner|There's an error in the code.|

---

## Use

- After successful deployment & WiFi connection the Pico will run one of the installed programs.
- Cycle through the installed programs by holding the Y button (bottom-right) for 2 seconds.

---

## Debug

* run `mpremote devs` to get your device address. E.g. `/dev/cu.usbmodem2101`
* `mpremote connect [put address here]`  then `ctrl D` to see outputs in the terminal
* `ctrl ]` to exit

---

## Resources

- [pico-up](https://pypi.org/project/pico-up/)
- Setting up a [project-specific virtual Python environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
