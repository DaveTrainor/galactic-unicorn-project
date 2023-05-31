import app.settings

import time
import math

#16*7

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# debounce reset button
# resetDebounce = 8

class Paddle:
    def __init__(self, devices, settings, x_start, colour):
        # Proper Pong has angled paddles must be three wide
        self.size = 3
        # if settings.screen.driver == 'pico_unicorn':
        #     self.size = 2
        # else:
        #     self.size = 3

        self.x = int(x_start)
        self.y = math.floor((devices.screen.attributes.height - self.size) / 2)
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
        self.y = math.floor(devices.screen.attributes.height / 2)
        self.startY = self.y
        self.startX = self.x

    def resetBall(self):
        self.x = self.startX
        self.y = self.startY

class PongGame:
    display_name = 'Pong'
    slow_load = False

    def __init__(self, devices, settings):
        self.devices = devices
        self.x_velocity = 1
        self.y_velocity = 0
        self.bounce_angle = 0.5
        self.left_paddle = Paddle(devices, settings, 1, RED)
        self.right_paddle = Paddle(devices, settings, devices.screen.attributes.width - 2, BLUE)
        self.ball = Ball(devices, devices.screen.attributes.width/2, GREEN)

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

    def start(self):
        while True:
            # print(f'AX:{self.left_paddle.x} AY:{self.left_paddle.y}')
            # print(f'BX:{self.right_paddle.x} BY:{self.right_paddle.y}')
            # print(f'BallX:{self.ball.x} BallY:{self.ball.y}')

            self.button_watcher(self.devices)

            self.devices.screen.clear()
            self.devices.screen.rectangle(((self.left_paddle.x, self.left_paddle.y), (1, self.left_paddle.size)), self.left_paddle.colour)
            self.devices.screen.rectangle(((self.right_paddle.x, self.right_paddle.y), (1, self.right_paddle.size)), self.right_paddle.colour)

            self.devices.screen.rectangle(((int(self.ball.x), int(math.floor(self.ball.y))), (1, 1)), self.ball.colour)
            self.ball.x += self.x_velocity
            self.ball.y += self.y_velocity

            # if ball reaches just before paddle, bounce
            if self.ball.x == self.devices.screen.attributes.width - 2: # right of screen

                print(f'BX:{self.right_paddle.x} BY:{self.right_paddle.y}')
                print(f'BallX:{self.ball.x} BallY:{self.ball.y}')

                if self.ballIsCentreOfPaddle(self.right_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                elif self.ballIsLowerEdgeOfPaddle(self.right_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                    self.y_velocity += self.bounce_angle
                elif self.ballIsUpperEdgeOfPaddle(self.right_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                    self.y_velocity -= self.bounce_angle

            elif self.ball.x == 1: # left of screen
                print(f'AX:{self.left_paddle.x} AY:{self.left_paddle.y}')
                print(f'BallX:{self.ball.x} BallY:{self.ball.y}')

                if self.ballIsCentreOfPaddle(self.left_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                elif self.ballIsLowerEdgeOfPaddle(self.left_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                    self.y_velocity += self.bounce_angle
                elif self.ballIsUpperEdgeOfPaddle(self.left_paddle, self.ball):
                    self.x_velocity = -self.x_velocity
                    self.y_velocity -= self.bounce_angle

            if self.ball.y <= 0 or self.ball.y >= (self.devices.screen.attributes.height - 1):
                self.y_velocity = -self.y_velocity

            #Someone has scored
            if (self.ball.x > (self.devices.screen.attributes.width - 1)):
                print("Left player has won!")
                self.doReset()
            elif(self.ball.x < 0):
                print("Right players has won!")
                self.doReset()

            time.sleep(0.1)
