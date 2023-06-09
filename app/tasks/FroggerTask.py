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

class Frog(Entity):
    def __init__(self, colour, height, width, x_start, y_start):
        super().__init__(colour, height, width, x_start, y_start)

    def update_position(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

# Task

class FroggerTask(BaseTask):

    def __init__(self, settings):
        super().__init__(settings)
        self.display_width = 15
        self.display_height = 6

        self.colour_green = (100, 255, 100)
        self.colour_red = (255, 50, 50)

    def start(self):
        self.entity = Entity(self.colour_red, 2, 2, 2, 5)
        self.frog = Frog(self.colour_green, 1, 1, 1, 3)

    def stop(self):
        pass

    def input(self, buttons):
        frog = self.frog

        x_change = 0
        y_change = 0

        if buttons['left_1']:
            y_change -= 1

        if buttons['left_2']:
            y_change += 1

        if buttons['right_1']:
            x_change += 1

        if buttons['right_2']:
            x_change -= 1

        new_frog_x = frog.x + x_change
        new_frog_y = frog.y + y_change

        if new_frog_x < 0 or new_frog_x > self.display_width:
            x_change = 0

        if new_frog_y < 0 or new_frog_y > self.display_height:
            y_change = 0

        frog.update_position(x_change, y_change)

    def state(self):
        pass

    def render(self, screen):
        screen.clear()
        screen.rectangle(*self.entity.get_properties())
        screen.rectangle(*self.frog.get_properties())
