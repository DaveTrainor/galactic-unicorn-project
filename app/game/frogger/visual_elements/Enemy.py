from app.game.utilities.VisualElement import VisualElement
from app.game.utilities.Counter import Counter

class Enemy(VisualElement):
    def __init__(self, colour, x_length, y_length, x_start, y_start, y_boundary, direction, velocity):
        super().__init__(colour, x_length, y_length, x_start, y_start)

        self.y_min = -y_length
        self.y_max = y_boundary
        self.direction = direction
        self.movement_counter = Counter(10 / velocity)

    def move(self):
        self.movement_counter.increment()

        if self.movement_counter.check_limit():
            if self.direction == 'down':
                self.y += 1
            if self.direction  == 'up':
                self.y -= 1
            self.movement_counter.reset()
            
        if self.direction == 'down' and self.y > self.y_max:
            self.y = self.y_min

        if self.direction == 'up' and self.y < self.y_min:
            self.y = self.y_max
