from app.utilities.Colours import Colours
from app.game.utilities.VisualElement import VisualElement

from .visual_elements.Frog import Frog
from .visual_elements.Enemy import Enemy

class Frogger():
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.colours = Colours()

        # Counters
        self.enemy_loop_counter = 0
        self.event_loop_counter = 0

        # State
        self.win_state = False
        self.loose_state = False
        self.lock_controls = False

        # Visual Elements
        self.start_area = VisualElement(self.colours.blue, 2, self.y_boundary + 1, 0, 0)
        self.goal_area = VisualElement(self.colours.blue, 2, self.y_boundary + 1, self.x_boundary - 1, 0)

        self.enemy_1 = Enemy(self.colours.purple, 2, 3, 4, -2, self.y_boundary, 'down', 2)
        self.enemy_2 = Enemy(self.colours.yellow, 2, 6, 8, self.y_boundary - 1, self.y_boundary, 'up', 1)
        self.enemy_3 = Enemy(self.colours.purple, 2, 3, 12, -2, self.y_boundary, 'down', 3)

        self.frog = Frog(self.colours.green_light, 1, 1, 1, 3, self.x_boundary, self.y_boundary)

        self.visual_elements = [self.start_area, self.goal_area, self.enemy_1, self.enemy_2, self.enemy_3, self.frog]

    # State Management
    def set_win_state(self, win_state):
        self.win_state = win_state

    def set_loose_state(self, loose_state):
        self.loose_state = loose_state

    def set_control_lock(self, lock_controls):
        self.lock_controls = lock_controls

    # Collision Detection
    def collision_detector(self, element_1, element_2, collision_event):
        x_min_1, x_max_1, y_min_1, y_max_1 = element_1.get_footprint()
        x_min_2, x_max_2, y_min_2, y_max_2 = element_2.get_footprint()

        if x_max_1 < x_min_2 or x_max_2 < x_min_1:
            return
        
        if y_max_1 < y_min_2 or y_max_2 < y_min_1:
            return
        
        collision_event()

    # Reset Game
    def reset_game(self):
        self.set_win_state(False)
        self.set_loose_state(False)
        self.set_control_lock(False)
        self.event_loop_counter = 0
        self.start_area.reset()
        self.goal_area.reset()
        self.frog.reset()

    # Check for Win / Loose
    def check_win_conditions(self):
        self.collision_detector(self.frog, self.goal_area, lambda: self.set_win_state(True))

    def check_loose_conditions(self):
        self.collision_detector(self.frog, self.enemy_1, lambda: self.set_loose_state(True))
        self.collision_detector(self.frog, self.enemy_2, lambda: self.set_loose_state(True))
        self.collision_detector(self.frog, self.enemy_3, lambda: self.set_loose_state(True))

    # Processes that use the game loop
    def enemy_movement(self):
        self.enemy_loop_counter += 1
        if self.enemy_loop_counter > 3:
            self.enemy_1.move()
            self.enemy_2.move()
            self.enemy_3.move()
            self.enemy_loop_counter = 0

    def loose_handler(self):
        self.check_loose_conditions()

        if self.loose_state is True:
            self.set_control_lock(True)
            self.event_loop_counter += 1
            self.start_area.change_colour(self.colours.red)
            self.goal_area.change_colour(self.colours.red)
            self.frog.change_colour(self.colours.red)

        if self.event_loop_counter > 60:
            self.reset_game()

    def win_handler(self):
        self.check_win_conditions()

        if self.win_state is True:
            self.set_control_lock(True)
            self.event_loop_counter += 1
            self.start_area.change_colour(self.colours.green)
            self.goal_area.change_colour(self.colours.green)

        if self.event_loop_counter > 60:
            self.reset_game()

    def loop_events(self):
        self.enemy_movement()
        self.win_handler()
        self.loose_handler()

    # Controls
    def button_watcher(self, button):
        if self.lock_controls is False:

            if button == 'left_1':
                self.frog.move(0, -1)
                
            if button == 'left_2':
                self.frog.move(0, 1)

            if button == 'right_1':
                self.frog.move(1, 0)

            if button == 'right_2':
                self.frog.move(-1, 0)
