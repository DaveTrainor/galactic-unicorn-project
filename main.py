import app.settings
from app.device import setup_devices


from picographics import PicoGraphics, PEN_RGB332
import time
import math

devices = setup_devices()
settings = app.settings.Settings()

# display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN, pen_type=PEN_RGB332)
# screen = GalacticUnicorn()
# screen = hardware
# display = abstract screen

x = 1
y = 0

x1 = devices.screen.attributes.width -2
y1 = 0

x2,y2 = 3, math.floor(devices.screen.attributes.height/2)

# red = display.create_pen(255, 0, 0)
# blue = display.create_pen(0, 0, 255)
# green = display.create_pen(0, 255, 0)
# blank = display.create_pen(0, 0, 0)
x_velocity = 1.0
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    if devices.screen.is_pressed('left_1'):
        y = max(0, y - 1)
    elif devices.screen.is_pressed('left_4'):
        y = min(devices.screen.attributes.height - 2, y + 1)
        
    if devices.screen.is_pressed('right_1'):
        y1 = max(0, y1 - 1)
    elif devices.screen.is_pressed('right_4'):
        y1 = min(devices.screen.attributes.height - 2, y1 + 1)

    devices.screen.clear()
    devices.screen.clear(((x, y),(1,2)),RED)


    devices.screen.clear(((x1, y1), (1, 2)), BLUE)
    devices.screen.clear(((int(x2), y2), (1, 1)), GREEN)
    x2 += x_velocity

    if x2 == devices.screen.attributes.width - 3 and (y1 == y2 or y1+1 == y2):
        x_velocity = -x_velocity
    elif x2 == 2 and (y == y2 or y+1 == y2):
        x_velocity = -x_velocity


    time.sleep(0.1)



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
# >>>>>>> feat/framework-updates
