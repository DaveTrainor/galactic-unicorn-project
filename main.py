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



class MainMenu:
    def __init__(self):
        self.left_button_message = 'A: Pong'
        self.right_button_message = 'B: Time / Temp'
        self.left_button_page = Page([
            PageSection(PageSectionType.TEXT, (self.left_button_message, (0, 255, 0))),
        ])
        self.right_button_page = Page([
            PageSection(PageSectionType.TEXT, (self.right_button_message, (0, 0, 255))),
        ])
        self.keep_running = True
        asyncio.run(self.main_loop())

    async def button_watcher(self):
        print('button watcher started')
        while self.keep_running:
            if devices.screen.is_pressed('left_1'):
                self.keep_running = False
                pong.play_pong(devices, settings)

            elif devices.screen.is_pressed('left_2'):
                self.keep_running = False
                devices.screen.clear()
                self.time_text_loading_page = Page([
                    PageSection(PageSectionType.TEXT, ('Loading...', (0, 255, 0))),
                ])
                devices.screen.show_page(self.time_text_loading_page)
                time_and_temp.TimeTemp(devices, settings)
            await asyncio.sleep(0.1)

    async def show_menu(self):
        while self.keep_running:
            devices.screen.clear()
            devices.screen.show_page(self.left_button_page)
            await asyncio.sleep(2)
            devices.screen.clear()
            devices.screen.show_page(self.right_button_page)
            await asyncio.sleep(2)

    async def main_loop(self):
        print('Main loop started')
        asyncio.create_task(self.show_menu())
        await asyncio.create_task(self.button_watcher())


MainMenu()

