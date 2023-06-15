from app.game.utilities.VisualElement import VisualElement

class Frog(VisualElement):
    def __init__(self, colour, x_length, y_length, x_start, y_start, x_limit, y_limit):
        super().__init__(colour, x_length, y_length, x_start, y_start)

        self.x_limit = x_limit
        self.y_limit = y_limit

    def move(self, x_change, y_change):
        new_x = self.x + x_change
        new_y = self.y + y_change

        if new_x >= 0 and new_x <= self.x_limit:
            self.x = new_x

        if new_y >= 0 and new_y <=self.y_limit:
            self.y = new_y
