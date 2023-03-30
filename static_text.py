import time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN


gu=GalacticUnicorn()
graphics=PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)
green_pen=graphics.create_pen(20, 20, 100)


graphics.set_font("bitmap6")
graphics.set_pen(green_pen)
graphics.text("Hello everyone!",0, -1, True, scale=0.5)
gu.update(graphics)
    