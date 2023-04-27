import time
import app.settings
from app.device import setup_devices
from app.game import pong
from app.widgets import time_and_temp
from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType
import uasyncio as asyncio

devices = setup_devices()
settings = app.settings.Settings()


async def button_watcher():
    print('button watcher started')
    while True:
        if devices.screen.is_pressed('left_1'):
            pong.play_pong(devices, settings)

        elif devices.screen.is_pressed('left_2'):
            time_and_temp.TimeTemp(devices,settings)
        await asyncio.sleep(0.1)


left_button_message = 'A: Pong'
right_button_message = 'B: Time / Temp'

left_button_page = Page([
                PageSection(PageSectionType.TEXT, (left_button_message, (0, 255, 0))),
                ])

right_button_page = Page([
                PageSection(PageSectionType.TEXT, (right_button_message, (0, 0, 255))),
                ])


async def show_menu():
    while True:
        devices.screen.clear()
        devices.screen.show_page(left_button_page)
        await asyncio.sleep(2)
        devices.screen.clear()
        devices.screen.show_page(right_button_page)
        await asyncio.sleep(2)


async def main_loop():
    print('Main loop started')
    task_1 = asyncio.create_task(button_watcher())
    task_2 = asyncio.create_task(show_menu())

    await task_1
    await task_2

asyncio.run(main_loop())


