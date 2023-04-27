import uasyncio as asyncio


from app.clients.TimeClient import TimeClient
from app.clients.WeatherForecastClient import WeatherForecastClient

from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType


class TimeTemp:

    def __init__(self, devices, settings):
        self.settings = settings
        self.devices = devices
        self.weather_client = WeatherForecastClient()
        self.time_client = TimeClient()
        asyncio.run(self.main_loop())

    def show_time(self):
        while True:
            current_time = self.time_client.get_time()
            time_page = Page([
                PageSection(PageSectionType.TEXT, (current_time, (255, 255, 255))),
            ])
            self.devices.screen.clear()
            self.devices.screen.show_page(time_page)
            await asyncio.sleep(30)

    def show_weather(self):
        while True:
            current_temp, temp_colour = self.weather_client.get_temperature(self.settings.locale.coordinates)
            time_page = Page([
                PageSection(PageSectionType.TEXT, (current_temp, temp_colour)),
            ])
            self.devices.screen.clear()
            self.devices.screen.show_page(time_page)
            await asyncio.sleep(30)


    def animate_screen(self):
        while True:
            self.devices.screen.clear()
            self.devices.screen.next_frame()
            await asyncio.sleep(0.1)


    async def main_loop(self):
        try:
            # asyncio.create_task(animate_screen())
            asyncio.create_task(self.show_time())
            await asyncio.sleep(15)
            asyncio.create_task(self.show_weather())
            while True:
                await asyncio.sleep(1)
        except Exception as e:
            self.devices.screen.show_error(e)



