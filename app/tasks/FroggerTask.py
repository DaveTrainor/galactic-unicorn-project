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

    def reset(self):
        self.x = self.x_start
        self.y = self.y_start

class MovingEntity(Entity):
    def __init__(self, colour, height, width, x_start, y_start, x_limit, y_limit):
        super().__init__(colour, height, width, x_start, y_start)

        self.x_limit = x_limit
        self.y_limit = y_limit

    def update_position(self, x_change, y_change):
        new_x = self.x + x_change
        new_y = self.y + y_change

        if new_x >= 0 and new_x <= self.x_limit:
            self.x = new_x

        if new_y >= 0 and new_y <=self.y_limit:
            self.y = new_y

class Frog(MovingEntity):
    def __init__(self, colour, height, width, x_start, y_start, x_limit, y_limit):
        super().__init__(colour, height, width, x_start, y_start, x_limit, y_limit)


# Game

class FroggerGame():
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary

        self.colour_red = (255, 50, 50)
        self.colour_green = (100, 255, 100)

        self.frog = Frog(self.colour_green, 1, 1, 1, 3, self.x_boundary, self.y_boundary)

    def button_watcher(self, input):
        if input == 'left_1':
            self.frog.update_position(0, -1)
            
        if input == 'left_2':
            self.frog.update_position(0, 1)

        if input == 'right_1':
            self.frog.update_position(1, 0)

        if input == 'right_2':
            self.frog.update_position(-1, 0)


# Task

class FroggerTask(BaseTask):
    def __init__(self, settings):
        super().__init__(settings)
        self.display_width = 15
        self.display_height = 6

    def start(self):
        self.game = FroggerGame(self.display_width, self.display_height)

    def stop(self):
        pass

    def input(self, buttons):
        if buttons['left_1']:
            self.game.button_watcher('left_1')

        if buttons['left_2']:
            self.game.button_watcher('left_2')

        if buttons['right_1']:
            self.game.button_watcher('right_1')

        if buttons['right_2']:
            self.game.button_watcher('right_2')

    def state(self):
        pass

    def render(self, screen):
        screen.clear()
        screen.rectangle(*self.game.frog.get_properties())
