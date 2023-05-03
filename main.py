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


class LoadingScreen:
    def __init__(self, devices):
        devices.screen.clear()
        self.page = Page([
            PageSection(PageSectionType.TEXT, ('Loading...', (180, 0, 160))),
    ])
        devices.screen.show_page(self.page)
class MainMenu:
    def __init__(self):
        self.action_button_A = pong.PongGame
        self.action_button_B = time_and_temp.TimeTemp
        self.left_button_message = f'A: {self.action_button_A.display_name}'
        self.right_button_message = f'B: {self.action_button_B.display_name}'
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
                loading_screen = LoadingScreen(devices)
                new_action = self.action_button_A(devices, settings)
                new_action.start()

            elif devices.screen.is_pressed('left_2'):
                self.keep_running = False
                loading_screen = LoadingScreen(devices)
                new_action = self.action_button_B(devices, settings)
                new_action.start()
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

