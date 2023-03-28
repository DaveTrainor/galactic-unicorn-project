from .BaseScreen import BaseScreen
from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK


class PicoUnicornScreen(BaseScreen):
    def __init__(self):
        self.screen = PicoUnicorn()
        self.display = PicoGraphics(display=DISPLAY_UNICORN_PACK)
        self.pens = {
            'WHITE': self.display.create_pen(100, 100, 100)
        }

    def show_text(self, text):
        self.display.set_font('bitmap6')
        self.display.set_pen(self.pens.get('WHITE'))
        self.display.text(text, 1, 0, scale=0.1)
        self.screen.update(self.display)
