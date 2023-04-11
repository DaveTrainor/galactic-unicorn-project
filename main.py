import uasyncio as asyncio

from app.clients.TimeClient import TimeClient
from app.clients.WeatherForecastClient import WeatherForecastClient
from app.device import setup_devices
from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType

devices = setup_devices()
weather_client = WeatherForecastClient()
time_client = TimeClient()
try:
    def slideshow():
        while True:
            current_time = time_client.get_time()
            time_page = Page([
                # PageSection(PageSectionType.SPRITE, ('icons', (0, 0))),
                # PageSection(PageSectionType.TEXT, ('Hello!', (100, 100, 100))),
                PageSection(PageSectionType.TEXT, (current_time, (255, 255, 255))),
            ])
            devices.screen.clear()
            devices.screen.show_page(time_page)
            await asyncio.sleep(30)

    def animate_screen():
        while True:
            devices.screen.clear()
            devices.screen.next_frame()
            await asyncio.sleep(0.1)

    async def main_loop():
        asyncio.create_task(slideshow())
        asyncio.create_task(animate_screen())
        while True:
            await asyncio.sleep(1)


    asyncio.run(main_loop())
except Exception as e:
    devices.screen.show_error(e)
