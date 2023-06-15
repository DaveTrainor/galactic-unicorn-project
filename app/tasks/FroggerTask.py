from app.game.frogger.Frogger import Frogger
from .BaseTask import BaseTask

class FroggerTask(BaseTask):
    def __init__(self, settings):
        super().__init__(settings)
        self.display_x_length = 15
        self.display_y_length = 6
        self.game = Frogger(self.display_x_length, self.display_y_length)

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
        self.game.loops()

    def render(self, screen):
        screen.clear()

        for element in self.game.visual_elements:
            screen.rectangle(*element.get_rectangle_properties())
