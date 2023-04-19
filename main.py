from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN, PEN_RGB332
import time
import math

display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN, pen_type=PEN_RGB332)
screen = GalacticUnicorn()
# screen = hardware
# display = abstract screen
x = 1
y = 0

x1 = screen.WIDTH -2
y1 = 0

x2,y2 = 3, math.floor(screen.HEIGHT/2)

red = display.create_pen(255, 0, 0)
blue = display.create_pen(0, 0, 255)
green = display.create_pen(0, 255, 0)
blank = display.create_pen(0, 0, 0)
x_velocity = 1.0

while True:
    if screen.is_pressed(screen.SWITCH_A):
        y = max(0, y - 1)
    elif screen.is_pressed(screen.SWITCH_D):
        y = min(screen.HEIGHT - 2, y + 1)
        
    if screen.is_pressed(screen.SWITCH_VOLUME_UP):
        y1 = max(0, y1 - 1)
    elif screen.is_pressed(screen.SWITCH_BRIGHTNESS_DOWN):
        y1 = min(screen.HEIGHT - 2, y1 + 1)

    display.set_pen(blank)
    display.clear()
    display.set_pen(red)
    display.pixel(x, y)
    display.pixel(x, y+1)
    
    display.set_pen(blue)
    display.pixel(x1, y1)
    display.pixel(x1, y1+1)

    display.set_pen(green)
    display.pixel(int(x2), y2)
    x2 += x_velocity

    if x2 == screen.WIDTH - 3 and (y1 == y2 or y1+1 == y2):
        x_velocity = -x_velocity
    elif x2 == 2 and (y == y2 or y+1 == y2):
        x_velocity = -x_velocity


    screen.update(display)
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
