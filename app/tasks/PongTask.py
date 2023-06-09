from .BaseTask import BaseTask
from app.device.screen import BaseScreen
from app.settings import Settings
import time
import math


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

height = 7
width = 16

class Paddle:
    def __init__(self, x_start, colour):
        # Proper Pong has angled paddles must be three wide
        self.size = 3
        self.x = int(x_start)
        self.y = math.floor((height - self.size) / 2)
        self.colour = colour
        self.startY = self.y
        self.startX = self.x

    def resetPaddle(self):
        self.x = self.startX
        self.y = self.startY

class Ball:
    def __init__(self, devices, x_start, colour):
        self.colour = colour
        self.x = int(x_start)
        self.y = math.floor(height / 2)
        self.startY = self.y
        self.startX = self.x

    def resetBall(self):
        self.x = self.startX
        self.y = self.startY

class PongGame:
    display_name = 'Pong'
    slow_load = False

    def __init__(self):
        self.x_velocity = 1
        self.y_velocity = 0
        self.bounce_angle = 0.5
        self.left_paddle = Paddle(self.settings, 1, RED)
        self.right_paddle = Paddle(self.settings, width - 2, BLUE)
        self.ball = Ball(width/2, GREEN)

    def doReset(self):
        self.ball.resetBall()
        self.left_paddle.resetPaddle()
        self.right_paddle.resetPaddle()

        self.x_velocity = 1
        self.y_velocity = 0

        time.sleep(1)

        #   0123456789ABCDEF
        # 0 ****************
        # 1 *|************|*
        # 2 *|***********X|*
        # 3 *|************|*
        # 4 ****************
        # 5 ****************
        # 6 ****************

    def ballIsCentreOfPaddle(self, paddle, ball):
        return ball.y == paddle.y+1

    def ballIsUpperEdgeOfPaddle(self, paddle, ball):
        return ball.y == paddle.y

    def ballIsLowerEdgeOfPaddle(self, paddle, ball):
        return ball.y == (paddle.y + 2 )

    def button_watcher(self, devices):
        if devices.screen.is_pressed('left_1') and devices.screen.is_pressed('right_1'):
            self.doReset()

        if devices.screen.is_pressed('left_1'):
            self.left_paddle.y = max(0, self.left_paddle.y - 1)
        elif devices.screen.is_pressed('left_2'):
            self.left_paddle.y = min(devices.screen.attributes.height - self.left_paddle.size, self.left_paddle.y + 1)

        if devices.screen.is_pressed('right_1'):
            self.right_paddle.y = max(0, self.right_paddle.y - 1)
        elif devices.screen.is_pressed('right_2'):
            self.right_paddle.y = min(devices.screen.attributes.height - self.right_paddle.size, self.right_paddle.y + 1)


class PongTask(BaseTask):
    def __init__(self, settings):
        super().__init__(settings)

    def start(self):
        self.game = PongGame()

    def stop(self):
        self.game = None

    def input(self, buttons):
        if buttons['left_1'] and buttons['right_1']:
            self.game.doReset()

        if buttons['left_1']:
            self.left_paddle.y = max(0, self.left_paddle.y - 1)
        elif buttons['left_2']:
            self.left_paddle.y = min(height - self.left_paddle.size, self.left_paddle.y + 1)

        if buttons['right_1']:
            self.right_paddle.y = max(0, self.right_paddle.y - 1)
        elif buttons['right_2']:
            self.right_paddle.y = min(height - self.right_paddle.size, self.right_paddle.y + 1)

    def state(self):
        """Ran at regular intervals, this method should alter the state of the task based on the passage of time
        """
        raise NotImplementedError

    def render(self, screen: BaseScreen):
        screen.clear()
        screen.rectangle(((self.left_paddle.x, self.left_paddle.y), (1, self.left_paddle.size)), self.left_paddle.colour)
        screen.rectangle(((self.right_paddle.x, self.right_paddle.y), (1, self.right_paddle.size)), self.right_paddle.colour)

        screen.rectangle(((int(self.ball.x), int(math.floor(self.ball.y))), (1, 1)), self.ball.colour)
