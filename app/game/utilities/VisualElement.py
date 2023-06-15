class VisualElement:
    def __init__(self, colour, x_length, y_length, x_start, y_start):
        self.colour = colour
        self.x_length = x_length
        self.y_length = y_length
        self.x = x_start
        self.y = y_start

        self.x_start = x_start
        self.y_start = y_start
        self.colour_start = colour

    def get_rectangle_properties(self):
        return [((self.x, self.y), (self.x_length, self.y_length)), self.colour]

    def get_footprint(self):
        footprint = [self.x, self.x + self.x_length - 1, self.y, self.y + self.y_length - 1]
        return footprint

    def change_colour(self, colour):
        self.colour = colour

    def reset(self):
        self.x = self.x_start
        self.y = self.y_start
        self.colour = self.colour_start
