import app.settings
from app.device import setup_devices
from app.game import pong

devices = setup_devices()
settings = app.settings.Settings()

pong.play_pong(devices, settings)

#
# import uasyncio as asyncio
#
# import app.settings
# from app.clients.TimeClient import TimeClient
# from app.clients.WeatherForecastClient import WeatherForecastClient
# from app.device import setup_devices
# from app.page.Page import Page
# from app.page.PageSection import PageSection, PageSectionType
#
# devices = setup_devices()
# settings = app.settings.Settings()
#
# weather_client = WeatherForecastClient()
# time_client = TimeClient()
#
# try:
#     def show_time():
#         while True:
#             current_time = time_client.get_time()
#             time_page = Page([
#                 PageSection(PageSectionType.TEXT, (current_time, (255, 255, 255))),
#             ])
#             devices.screen.clear()
#             devices.screen.show_page(time_page)
#             await asyncio.sleep(30)
#
#
#     def show_weather():
#         while True:
#             current_temp, temp_colour = weather_client.get_temperature(settings.locale.coordinates)
#             time_page = Page([
#                 PageSection(PageSectionType.TEXT, (current_temp, temp_colour)),
#             ])
#             devices.screen.clear()
#             devices.screen.show_page(time_page)
#             await asyncio.sleep(30)
#
#
#     def animate_screen():
#         while True:
#             devices.screen.clear()
#             devices.screen.next_frame()
#             await asyncio.sleep(0.1)
#
#
#     async def main_loop():
#         # asyncio.create_task(animate_screen())
#         asyncio.create_task(show_time())
#         await asyncio.sleep(15)
#         asyncio.create_task(show_weather())
#         while True:
#             await asyncio.sleep(1)
#
#
#     asyncio.run(main_loop())
# except Exception as e:
#     devices.screen.show_error(e)
#
