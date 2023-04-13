from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK, PEN_RGB888
import time

display = PicoGraphics(display=DISPLAY_UNICORN_PACK, pen_type=PEN_RGB888)
screen = PicoUnicorn()
# screen = hardware
# display = abstract screen
x = 1
y = 0

red = display.create_pen(255, 0, 0)
blank = display.create_pen(0, 0, 0)

while True:
    if screen.is_pressed(screen.BUTTON_A):
        y = max(0, y - 1)
    elif screen.is_pressed(screen.BUTTON_B):
        y = min(screen.get_height() - 2, y + 1)
    
    display.set_pen(blank)
    display.clear()
    display.set_pen(red)
    display.pixel(x, y)
    display.pixel(x, y+1)
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