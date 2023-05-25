from .BaseTask import BaseTask


class ColourTask(BaseTask):
    colour: (int, int, int)

    def __init__(self, settings):
        super().__init__(settings)
        self.colour = (0, 100, 200)
        self.increment = 1

    def start(self):
        pass

    def stop(self):
        pass

    def input(self, buttons):
        if buttons['left_1']:
            self.increment += 1
        if buttons['left_2']:
            self.increment -= 1

        if self.increment < 1:
            self.increment = 1

        if self.increment > 10:
            self.increment = 10

    def state(self):
        r, b, g = self.colour
        r += self.increment
        b += self.increment
        g += self.increment

        if r > 255:
            r = 0
        if b > 255:
            b = 0
        if g > 255:
            g = 0

        self.colour = (r, b, g)

    def render(self, screen):
        screen.clear(colour=self.colour)
