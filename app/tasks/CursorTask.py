from .BaseTask import BaseTask

class CursorTask(BaseTask):

    def __init__(self, settings):
        super().__init__(settings)
        self.display_width = 15
        self.display_height = 6

        self.colour_background = (60, 10, 60)
        self.colour_cursor = (100, 255, 100)

        self.cursor_position_y = 3
        self.cursor_position_x = 0

    def start(self):
        pass

    def stop(self):
        pass

    def input(self, buttons):
        if buttons['left_1']:
            self.cursor_position_y -= 1

        if buttons['left_2']:
            self.cursor_position_y += 1

        if self.cursor_position_y < 0:
            self.cursor_position_y = 0

        if self.cursor_position_y > self.display_height:
            self.cursor_position_y = self.display_height

        if buttons['right_1']:
            self.cursor_position_x += 1

        if buttons['right_2']:
            self.cursor_position_x -= 1

        if self.cursor_position_x < 0:
            self.cursor_position_x = 0

        if self.cursor_position_x > self.display_width:
            self.cursor_position_x = self.display_width

    def state(self):
        pass

    def render(self, screen):
        screen.clear(colour = self.colour_background)
        screen.rectangle(((self.cursor_position_x, self.cursor_position_y), (1, 1)), self.colour_cursor)
