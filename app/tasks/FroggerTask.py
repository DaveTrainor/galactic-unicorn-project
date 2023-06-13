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
        self.x = x_start
        self.y = y_start

        self.x_start = x_start
        self.y_start = y_start
        self.colour_start = colour

    def get_render_properties(self):
        return [((self.x, self.y), (self.width, self.height)), self.colour]
    
    def change_colour(self, colour):
        self.colour = colour

    def reset(self):
        self.x = self.x_start
        self.y = self.y_start
        self.colour = self.colour_start


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


class Enemy(VisualElement):
    def __init__(self, colour, height, width, x_start, y_start, y_limit, direction, velocity):
        super().__init__(colour, height, width, x_start, y_start)

        self.y_limit = y_limit
        self.direction = direction
        self.velocity = velocity
        self.time_counter = 0

    def move(self):
        self.time_counter += self.velocity

        if self.time_counter >= 10:
            if self.direction == 'down':
                self.y += 1
            if self.direction  == 'up':
                self.y -= 1
            self.time_counter = 0

        if self.direction == 'down' and self.y > self.y_limit:
            self.y = self.y_start

        if self.direction == 'up' and self.y < -self.height:
            self.y = self.y_start


class FroggerGame():
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.colours = Colours()

        # Counters
        self.enemy_time_counter = 0
        self.event_time_counter = 0

        # State
        self.win_state = False
        self.loose_state = False

        # Visual Elements
        self.start_area = VisualElement(self.colours.blue, self.y_boundary + 1, 2, 0, 0)
        self.goal_area = VisualElement(self.colours.blue, self.y_boundary + 1, 2, self.x_boundary - 1, 0)

        self.enemy_1 = Enemy(self.colours.red, 3, 2, 4, -2, self.y_boundary, 'down', 2)
        self.enemy_2 = Enemy(self.colours.yellow, 6, 2, 8, self.y_boundary - 1, self.y_boundary, 'up', 1)
        self.enemy_3 = Enemy(self.colours.red, 3, 2, 12, -2, self.y_boundary, 'down', 3)

        self.frog = Frog(self.colours.green, 1, 1, 1, 3, self.x_boundary, self.y_boundary)

    # State Management

    def set_win_state(self, win_state):
        self.win_state = win_state

    def set_loose_state(self, loose_state):
        self.loose_state = loose_state

    # Collision Detection

    def collision_detector(self, element_1, element_2, collision_event):
        e1 = element_1
        e2 = element_2

        # The coordinates of the corners of the two elements.
        x_min_1 = e1.x
        x_max_1 = e1.x + e1.width - 1
        y_min_1 = e1.y
        y_max_1 = e1.y + e1.height - 1

        x_min_2 = e2.x
        x_max_2 = e2.x + e2.width - 1
        y_min_2 = e2.y
        y_max_2 = e2.y + e2.height - 1

        # Check if the elements overlap on both the x and y axes (ie. if they have collided)
        x_overlap = False
        y_overlap = False

        if x_min_1 <= x_min_2 <= x_max_1 or x_min_1 <= x_max_2 <= x_max_1:
            x_overlap = True

        if x_min_2 <= x_min_1 <= x_max_2 or x_min_2 <= x_max_1 <= x_max_2:
            x_overlap = True

        if y_min_1 <= y_min_2 <= y_max_1 or y_min_1 <= y_max_2 <= y_max_1:
            y_overlap = True

        if y_min_2 <= y_min_1 <= y_max_2 or y_min_2 <= y_max_1 <= y_max_2:
            y_overlap = True

        # If the elements have collided then invoke a method.
        if x_overlap and y_overlap:
            collision_event()

    # Processes that use the game loop

    def timed_events(self):

        # Enemy Movement
        self.enemy_time_counter += 1
        
        if self.enemy_time_counter > 3:
            self.enemy_1.move()
            self.enemy_2.move()
            self.enemy_3.move()
            self.enemy_time_counter = 0

        # Loose Game
        self.collision_detector(self.frog, self.enemy_1, lambda: self.set_loose_state(True))
        self.collision_detector(self.frog, self.enemy_2, lambda: self.set_loose_state(True))
        self.collision_detector(self.frog, self.enemy_3, lambda: self.set_loose_state(True))

        if self.loose_state is True:
            self.event_time_counter += 1
            self.start_area.change_colour(self.colours.red)
            self.goal_area.change_colour(self.colours.red)
            self.frog.change_colour(self.colours.red)

        if self.event_time_counter > 60:
            self.set_loose_state(False)
            self.event_time_counter = 0
            self.start_area.reset()
            self.goal_area.reset()
            self.frog.reset()

        # Win Game
        self.collision_detector(self.frog, self.goal_area, lambda: self.set_win_state(True))

        if self.win_state is True:
            self.event_time_counter += 1
            self.start_area.change_colour(self.colours.green)
            self.goal_area.change_colour(self.colours.green)

        if self.event_time_counter > 60:
            self.set_win_state(False)
            self.event_time_counter = 0
            self.start_area.reset()
            self.goal_area.reset()
            self.frog.reset()

    # Controls

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
        self.game.timed_events()

    def render(self, screen):
        screen.clear()

        screen.rectangle(*self.game.start_area.get_render_properties())
        screen.rectangle(*self.game.goal_area.get_render_properties())

        screen.rectangle(*self.game.enemy_1.get_render_properties())
        screen.rectangle(*self.game.enemy_2.get_render_properties())
        screen.rectangle(*self.game.enemy_3.get_render_properties())

        screen.rectangle(*self.game.frog.get_render_properties())
