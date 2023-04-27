import app.settings
from app.device import setup_devices
from app.game import pong
from app.widgets import time_and_temp

devices = setup_devices()
settings = app.settings.Settings()

# pong.play_pong(devices, settings)

time = time_and_temp.TimeTemp(devices, settings)
