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



# from picounicorn import PicoUnicorn
# from picographics import PicoGraphics, DISPLAY_UNICORN_PACK, PEN_RGB888
# import time

# # create a PicoGraphics framebuffer to draw into
# graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK, pen_type=PEN_RGB888)

# # create our GalacticUnicorn object
# gu = PicoUnicorn()

# # start position for scrolling (off the side of the display)
# scroll = float(-PicoUnicorn.WIDTH)

# # message to scroll
# MESSAGE = "Boo"

# # pen colours to draw with
# BLACK = graphics.create_pen(0, 0, 0)
# PURPLE = graphics.create_pen(255, 0, 255)

# while True:
#     # determine the scroll position of the text
#     width = graphics.measure_text(MESSAGE, 0.4)
#     scroll += 0.25
#     if scroll > width:
#       scroll = float(-PicoUnicorn.WIDTH)

#     # clear the graphics object
#     graphics.set_pen(BLACK)
#     graphics.clear()

#     # draw the text
#     graphics.set_pen(PURPLE)
#     # text, x, y, wordwrap, scale, angle, spacing
#     graphics.text(MESSAGE, round(0 - scroll), 0, scale=0.4)

#     # update the display
#     gu.update(graphics)

#     time.sleep(0.02)
