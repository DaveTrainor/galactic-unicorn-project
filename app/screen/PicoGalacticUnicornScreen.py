from .BaseScreen import BaseScreen
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN, PEN_RGB332


class PicoGalacticUnicornScreen(BaseScreen):
    def __init__(self):
        self.screen = GalacticUnicorn()
        self.display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN, pen_type=PEN_RGB332)
        self.pens = {
            'WHITE': self.display.create_pen(100, 100, 100)
        }

    def show_text(self, text):
        self.display.set_font('bitmap6')
        self.display.set_pen(self.pens.get('WHITE'))
        self.display.text(text, 1, 0, scale=0.1)
        self.screen.update(self.display)

    def show_sprite(self):
        self.display.load_spritesheet("app/sprites/pirate.rgb332")
        self.display.update()
        self.display.sprite(0, 0, 0, 0)
        self.screen.update(self.display)
