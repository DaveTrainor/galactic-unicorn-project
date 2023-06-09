from .BaseTask import BaseTask

# Entities

class Entity:
    def __init__(self, colour, height, width, x_start, y_start):
        self.colour = colour
        self.height = height
        self.width = width
        self.x_start = x_start
        self.y_start = y_start
        self.x = self.x_start
        self.y = self.y_start

    def get_properties(self):
        return [((self.x, self.y), (self.width, self.height)), self.colour]

    def reset_entity(self):
        self.x = self.x_start
        self.y = self.y_start

# Task

class FroggerTask(BaseTask):

    def __init__(self, settings):
        super().__init__(settings)
        self.display_width = 15
        self.display_height = 6

        self.colour_background = (20, 10, 20)
        self.colour_green = (100, 255, 100)
        self.colour_red = (255, 50, 50)

    def start(self):
        self.entity = Entity(self.colour_green, 2, 3, 1, 1)

    def stop(self):
        pass

    def input(self, buttons):
        pass

    def state(self):
        pass

    def render(self, screen):
        screen.clear(colour = self.colour_background)
        screen.rectangle(*self.entity.get_properties())
