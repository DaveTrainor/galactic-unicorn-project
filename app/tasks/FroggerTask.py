from .BaseTask import BaseTask

class Colours:
    def __init__(self):
        self.red = (255, 50, 50)
        self.green = (100, 255, 100)
        self.blue = (0, 0, 150)
        self.yellow = (255, 255, 20)


class VisualElement:
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


class Frog(VisualElement):
    def __init__(self, colour, height, width, x_start, y_start, x_limit, y_limit):
        super().__init__(colour, height, width, x_start, y_start)

        self.x_limit = x_limit
        self.y_limit = y_limit

    def move(self, x_change, y_change):
        new_x = self.x + x_change
        new_y = self.y + y_change

        if new_x >= 0 and new_x <= self.x_limit:
            self.x = new_x

        if new_y >= 0 and new_y <=self.y_limit:
            self.y = new_y


class FroggerGame():
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.colours = Colours()

        self.starting_area = VisualElement(self.colours.blue, self.y_boundary + 1, 2, 0, 0)
        self.goal_area = VisualElement(self.colours.blue, self.y_boundary + 1, 2, self.x_boundary - 1, 0)

        self.frog = Frog(self.colours.green, 1, 1, 1, 3, self.x_boundary, self.y_boundary)

    def button_watcher(self, button):
        if button == 'left_1':
            self.frog.move(0, -1)
            
        if button == 'left_2':
            self.frog.move(0, 1)

        if button == 'right_1':
            self.frog.move(1, 0)

        if button == 'right_2':
            self.frog.move(-1, 0)


class FroggerTask(BaseTask):
    def __init__(self, settings):
        super().__init__(settings)
        self.display_width = 15
        self.display_height = 6
        self.game = FroggerGame(self.display_width, self.display_height)

    def start(self):
        pass

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

        screen.rectangle(*self.game.starting_area.get_properties())
        screen.rectangle(*self.game.goal_area.get_properties())

        screen.rectangle(*self.game.frog.get_properties())
