import app.settings
from app.device import setup_devices

import time
import math

devices = setup_devices()
settings = app.settings.Settings()

x_velocity = 1.0
paddle_size = 3
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



left_paddle = {'x': 1,
               'y': math.floor(devices.screen.attributes.height / 2),
               'colour': RED}

right_paddle = {'x': devices.screen.attributes.width -2,
                'y': math.floor(devices.screen.attributes.height / 2),
                'colour': BLUE}

ball = {'x': 3,
        'y': math.floor(devices.screen.attributes.height / 2),
        'colour': GREEN}


def button_watcher():
    if devices.screen.is_pressed('left_1'):
        left_paddle['y'] = max(0, left_paddle['y'] - 1)
    elif devices.screen.is_pressed('left_4'):
        left_paddle['y'] = min(devices.screen.attributes.height - paddle_size, left_paddle['y'] + 1)

    if devices.screen.is_pressed('right_1'):
        right_paddle['y'] = max(0, right_paddle['y'] - 1)
    elif devices.screen.is_pressed('right_4'):
        right_paddle['y'] = min(devices.screen.attributes.height - paddle_size, right_paddle['y'] + 1)


while True:
    button_watcher()

    devices.screen.clear()
    devices.screen.rectangle(((left_paddle['x'], left_paddle['y']), (1, paddle_size)), left_paddle['colour'])

    devices.screen.rectangle(((right_paddle['x'], right_paddle['y']), (1, paddle_size)), right_paddle['colour'])
    devices.screen.clear(((int(ball['x']), ball['y']), (1, 1)), ball['colour'])
    ball['x'] += x_velocity

    if ball['x'] == devices.screen.attributes.width - 3 and\
            (right_paddle['y'] <= ball['y'] <= right_paddle['y'] + paddle_size-1):
        x_velocity = -x_velocity
    elif ball['x'] == 2 and (left_paddle['y'] <= ball['y'] <= left_paddle['y'] + paddle_size-1):
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

