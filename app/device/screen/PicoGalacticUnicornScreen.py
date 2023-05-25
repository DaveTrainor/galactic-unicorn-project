import time

from .BaseScreen import BaseScreen, ScreenAttributes
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN, PEN_RGB332
from app.settings import ScreenSettings
from app.page.Page import Page


class PicoGalacticUnicornScreen(BaseScreen):
    attributes = ScreenAttributes(sprite_size=8, sprite_extension='rgb332', width=53, height=11)
    dimness = 2

    def __init__(self, settings: ScreenSettings):
        super().__init__(settings)
        self.screen = GalacticUnicorn()
        self.display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN, pen_type=PEN_RGB332)
        self.display.set_font('bitmap6')
        self.buttons = {
            'left_1': GalacticUnicorn.SWITCH_A,
            'left_2': GalacticUnicorn.SWITCH_B,
            'left_3': GalacticUnicorn.SWITCH_C,
            'left_4': GalacticUnicorn.SWITCH_D,
            'right_1': GalacticUnicorn.SWITCH_VOLUME_UP,
            'right_2': GalacticUnicorn.SWITCH_VOLUME_DOWN,
            'right_3': GalacticUnicorn.SWITCH_BRIGHTNESS_UP,
            'right_4': GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN,
        }

    def colour_correction(self, colour):
        r, g, b = colour

        r = int(r / self.dimness)
        g = int(g / self.dimness)
        b = int(b / self.dimness)
        return [r, g, b]

    def load_page(self, page: Page):
        self.current_page = page

    def show_text(self, position, text, colour=(100, 100, 100)):
        print(text)
        self.display.set_font('bitmap6')
        self.display.set_pen(self.display.create_pen(*self.colour_correction(colour)))
        self.display.text(text, position[0], position[1], scale=1)
        self.screen.update(self.display)
        return self

    def show_sprite(self):
        self.display.load_spritesheet("app/sprites/pirate.rgb332")
        self.display.update()
        self.display.sprite(4, 0, 0, 0)
        self.screen.update(self.display)

    def show_pixel(self, x, y):
        self.display.set_pen(self.pens.get('WHITE'))
        self.display.pixel(x, y)
        self.screen.update(self.display)

    def show_line(self, x1, y1, x2, y2, colour):
        self.display.set_pen(self.pens.get(colour))
        self.display.line(x1, y1, x2, y2)
        self.screen.update(self.display)

    def show_lines(self, p1, c1, p2, c2, p3, c3):
        self.display.set_pen(self.pens.get(c1))
        self.display.line(p1, 0, p1, 11)
        self.display.set_pen(self.pens.get(c2))
        self.display.line(p2, 0, p2, 11)
        self.display.set_pen(self.pens.get(c3))
        self.display.line(p3, 0, p3, 11)
        self.screen.update(self.display)
