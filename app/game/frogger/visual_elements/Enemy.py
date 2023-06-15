from app.game.utilities.VisualElement import VisualElement

class Enemy(VisualElement):
    def __init__(self, colour, x_length, y_length, x_start, y_start, y_limit, direction, velocity):
        super().__init__(colour, x_length, y_length, x_start, y_start)

        self.y_limit = y_limit
        self.direction = direction
        self.velocity = velocity
        self.movement_counter = 0

    def move(self):
        self.movement_counter += self.velocity

        if self.movement_counter >= 10:
            if self.direction == 'down':
                self.y += 1
            if self.direction  == 'up':
                self.y -= 1
            self.movement_counter = 0

        if self.direction == 'down' and self.y > self.y_limit:
            self.y = self.y_start

        if self.direction == 'up' and self.y < -self.y_length:
            self.y = self.y_start
