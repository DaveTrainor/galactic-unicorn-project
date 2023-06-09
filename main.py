import app.settings
from app.TaskManager import start_manager
from app.device import setup_devices
import uasyncio as asyncio

from app.tasks.CursorTask import CursorTask
from app.tasks.ColourTask import ColourTask
from app.tasks.TimeScrollerTask import TimeScrollerTask

devices = setup_devices()
settings = app.settings.Settings()

start_manager(asyncio,
    tasks=[
        CursorTask(settings),
        ColourTask(settings),
        TimeScrollerTask(settings),
    ],
    devices=devices,
    settings=settings)
