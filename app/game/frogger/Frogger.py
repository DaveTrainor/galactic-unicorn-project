from app.utilities.Colours import Colours
from app.game.utilities.State import State
from app.game.utilities.Counter import Counter
from app.game.utilities.VisualElement import VisualElement
from app.game.utilities.collision_detector import collision_detector
from .visual_elements.Frog import Frog
from .visual_elements.Enemy import Enemy

class Frogger():
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary

        # Colours
        self.colours = Colours()

        # State
        self.win_state = State(False)
        self.loose_state = State(False)
        self.lock_controls = State(False)

        # Loop Counters
        self.win_event_counter = Counter(60)
        self.loose_event_counter = Counter(60)
        self.enemy_movement_counter = Counter(3)

        # Visual Elements
        self.start_area = VisualElement(self.colours.blue, 2, self.y_boundary + 1, 0, 0)
        self.goal_area = VisualElement(self.colours.blue, 2, self.y_boundary + 1, self.x_boundary - 1, 0)

        self.enemy_1 = Enemy(self.colours.purple, 2, 3, 3, -2, self.y_boundary, 'down', 2)
        self.enemy_2 = Enemy(self.colours.yellow, 2, 6, 6, self.y_boundary - 1, self.y_boundary, 'up', 1)
        self.enemy_3 = Enemy(self.colours.purple, 2, 3, 9, -2, self.y_boundary, 'down', 3)
        self.enemy_4 = Enemy(self.colours.white, 1, 2, 12, -2, self.y_boundary, 'down', 3)
        self.enemy_5 = Enemy(self.colours.white, 1, 2, 13, -2, self.y_boundary, 'down', 5)

        self.frog = Frog(self.colours.green_light, 1, 1, 1, 3, self.x_boundary, self.y_boundary)

        self.visual_elements = [self.start_area, self.goal_area, self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4, self.enemy_5, self.frog]
        self.enemies = [self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4, self.enemy_5]

    # Check for Win / Loose
    def check_win_conditions(self):
        if collision_detector(self.frog, self.goal_area):
            self.win_state.set(True)

    def check_loose_conditions(self):
        for enemy in self.enemies:
            if collision_detector(self.frog, enemy):
                self.loose_state.set(True)

    # Reset Game
    def reset_game(self):
        self.win_state.reset()
        self.loose_state.reset()
        self.lock_controls.reset()
        self.win_event_counter.reset()
        self.loose_event_counter.reset()
        self.start_area.reset()
        self.goal_area.reset()
        self.frog.reset()

    # Processes that use the game loop
    def enemy_movement_loop(self):
        self.enemy_movement_counter.increment()
        if self.enemy_movement_counter.check_limit() is True:
            for enemy in self.enemies:
                enemy.move()

    def loose_event_loop(self):
        self.check_loose_conditions()

        if self.loose_state.get() is True:
            self.lock_controls.set(True)
            self.loose_event_counter.increment()
            self.start_area.change_colour(self.colours.red)
            self.goal_area.change_colour(self.colours.red)
            self.frog.change_colour(self.colours.red)

        if self.loose_event_counter.check_limit() is True:
            self.reset_game()

    def win_event_loop(self):
        self.check_win_conditions()

        if self.win_state.get() is True:
            self.lock_controls.set(True)
            self.win_event_counter.increment()
            self.start_area.change_colour(self.colours.green)
            self.goal_area.change_colour(self.colours.green)

        if self.win_event_counter.check_limit() is True:
            self.reset_game()

    def loops(self):
        self.enemy_movement_loop()
        self.win_event_loop()
        self.loose_event_loop()

    # Controls
    def button_watcher(self, button):
        if self.lock_controls.get() is False:

            if button == 'left_1':
                self.frog.move(0, -1)
                
            if button == 'left_2':
                self.frog.move(0, 1)

            if button == 'right_1':
                self.frog.move(1, 0)

            if button == 'right_2':
                self.frog.move(-1, 0)
