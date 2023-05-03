import app.settings

import time
import math



RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Paddle:
    def __init__(self, devices, settings, x_start, colour):
        if settings.screen.driver == 'pico_unicorn':
            self.size = 2
        else:
            self.size = 3
        self.x = int(x_start)
        self.y = math.floor((devices.screen.attributes.height - self.size) / 2)
        self.colour = colour


class Ball:
    def __init__(self, devices, x_start, colour):
        self.colour = colour
        self.x = x_start
        self.y = math.floor(devices.screen.attributes.height / 2)




class PongGame:
    display_name = 'Pong'
    slow_load = False

    def __init__(self, devices, settings):
        self.devices = devices
        self.x_velocity = 1.0
        self.left_paddle = Paddle(devices, settings, 1, RED)
        self.right_paddle = Paddle(devices, settings, devices.screen.attributes.width - 2, BLUE)
        self.ball = Ball(devices, 3, GREEN)

    def button_watcher(self, devices, left_paddle, right_paddle):
        if devices.screen.is_pressed('left_1'):
            self.left_paddle.y = max(0, self.left_paddle.y - 1)
        elif devices.screen.is_pressed('left_2'):
            self.left_paddle.y = min(devices.screen.attributes.height - self.left_paddle.size, self.left_paddle.y + 1)

        if devices.screen.is_pressed('right_1'):
            self.right_paddle.y = max(0, right_paddle.y - 1)
        elif devices.screen.is_pressed('right_2'):
            self.right_paddle.y = min(devices.screen.attributes.height - self.right_paddle.size, self.right_paddle.y + 1)

    def start(self):
        while True:
            self.button_watcher(self.devices, self.left_paddle, self.right_paddle)

            self.devices.screen.clear()
            self.devices.screen.rectangle(((self.left_paddle.x, self.left_paddle.y), (1, self.left_paddle.size)), self.left_paddle.colour)

            self.devices.screen.rectangle(((self.right_paddle.x, self.right_paddle.y), (1, self.right_paddle.size)), self.right_paddle.colour)
            self.devices.screen.clear(((int(self.ball.x), self.ball.y), (1, 1)), self.ball.colour)
            self.ball.x += self.x_velocity

            if self.ball.x == self.devices.screen.attributes.width - 3 and\
                    (self.right_paddle.y <= self.ball.y <= self.right_paddle.y + self.right_paddle.size-1):
                self.x_velocity = -self.x_velocity
            elif self.ball.x == 2 and (self.left_paddle.x <= self.ball.y <= self.left_paddle.y + self.left_paddle.size-1):
                self.x_velocity = -self.x_velocity

            time.sleep(0.1)
