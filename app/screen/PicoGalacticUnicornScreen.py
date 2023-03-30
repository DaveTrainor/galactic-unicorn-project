import time

from .BaseScreen import BaseScreen
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN, PEN_RGB332


class PicoGalacticUnicornScreen(BaseScreen):
    def __init__(self):
        self.screen = GalacticUnicorn()
        self.display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN, pen_type=PEN_RGB332)
        self.pens = {
            'WHITE': self.display.create_pen(100, 100, 100),
            'BLACK': self.display.create_pen(0, 0, 0),
            'RED': self.display.create_pen(100, 10, 10),
            'GREEN': self.display.create_pen(10, 100, 10),
            'BLUE': self.display.create_pen(10, 10, 100),
        }

    def show_text(self, text, alignment, colour):
        scale = 2
        thickness = 2
        self.display.set_font('bitmap6')
        self.display.set_thickness(thickness)
        self.display.set_pen(self.pens.get(colour))
        text_width = self.display.measure_text(text,scale)
        width, height = self.display.get_bounds()
        if alignment == 'centre':
            start_x = int((width-text_width)/2)+2
        self.display.text(text, start_x, -1, scale=scale)
        self.screen.update(self.display)

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

    def scroll_lines(self, p1, spacing, c1, c2, c3, thickness):
        while True:
            if p1 >= 53:
                p1 = 0

            p2 = p1 + spacing
            if p2 >= 53:
                p2 -= 53

            p3 = p1 + 2 * spacing
            if p3 >= 53:
                p3 -= 53

            self.display.set_pen(self.pens.get('BLACK'))
            self.display.clear()
            self.display.set_pen(self.pens.get(c1))
            self.display.line(p1, 0, p1, 11, thickness)
            self.display.set_pen(self.pens.get(c2))
            self.display.line(p2, 0, p2, 11, thickness)
            self.display.set_pen(self.pens.get(c3))
            self.display.line(p3, 0, p3, 11, thickness)
            self.screen.update(self.display)
            p1 += 1
            time.sleep(0.05)






