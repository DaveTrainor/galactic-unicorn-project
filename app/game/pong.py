import app.settings

import time
import math



RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Paddle:
    def __init__(self, settings, devices, x_start, colour):
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


def button_watcher(devices, left_paddle, right_paddle):
    if devices.screen.is_pressed('left_1'):
        left_paddle.y = max(0, left_paddle.y - 1)
    elif devices.screen.is_pressed('left_2'):
        left_paddle.y = min(devices.screen.attributes.height - left_paddle.size, left_paddle.y + 1)

    if devices.screen.is_pressed('right_1'):
        right_paddle.y = max(0, right_paddle.y - 1)
    elif devices.screen.is_pressed('right_2'):
        right_paddle.y = min(devices.screen.attributes.height - right_paddle.size, right_paddle.y + 1)


# class Game(self)

def play_pong(devices, settings):
    x_velocity = 1.0
    left_paddle = Paddle(settings, devices, 1, RED)
    right_paddle = Paddle(settings, devices, devices.screen.attributes.width - 2, BLUE)
    ball = Ball(devices, 3, GREEN)

    while True:
        button_watcher(devices, left_paddle, right_paddle)

        devices.screen.clear()
        devices.screen.rectangle(((left_paddle.x, left_paddle.y), (1, left_paddle.size)), left_paddle.colour)

        devices.screen.rectangle(((right_paddle.x, right_paddle.y), (1, right_paddle.size)), right_paddle.colour)
        devices.screen.clear(((int(ball.x), ball.y), (1, 1)), ball.colour)
        ball.x += x_velocity

        if ball.x == devices.screen.attributes.width - 3 and\
                (right_paddle.y <= ball.y <= right_paddle.y + right_paddle.size-1):
            x_velocity = -x_velocity
        elif ball.x == 2 and (left_paddle.x <= ball.y <= left_paddle.y + left_paddle.size-1):
            x_velocity = -x_velocity

        time.sleep(0.1)
