import time

from app.device.network import load_network, BaseNetwork
from app.device.screen import load_screen, BaseScreen
from app.settings import Settings


class Devices:
    screen: BaseScreen
    network: BaseNetwork


def setup_devices() -> Devices:
    print('[devices] setting up')
    settings = Settings()
    devices = Devices()

    print('[devices.screen] loading driver')
    devices.screen = load_screen(settings.screen)
    devices.screen.clear(((0, 0), (1, devices.screen.attributes.height)), colour=(0, 255, 0))
    print('[devices.screen] driver loaded')

    print('[devices.network] loading driver')
    devices.network = load_network(settings.network)
    print('[devices.network] driver loaded')
    print('[devices.network] connecting')
    devices.network.connect()

    while not devices.network.is_connected():
        devices.screen.clear(((1, 0), (1, devices.screen.attributes.height)), colour=(0, 0, 255))
        print('[devices.network] still connecting...')
        time.sleep(0.2)
        devices.screen.clear(((1, 0), (1, devices.screen.attributes.height)), colour=(0, 0, 0))
        time.sleep(0.2)

    print('[devices.network] connected')
    devices.screen.clear(((1, 0), (1, devices.screen.attributes.height)), colour=(0, 255, 0))

    time.sleep(0.5)

    for _ in range(4):
        devices.screen.clear(((0, 0), (devices.screen.attributes.width, devices.screen.attributes.height)),
                             colour=(0, 255, 0))
        time.sleep(0.05)
        devices.screen.clear()
        time.sleep(0.05)

    print('[devices] finished setting up')

    return devices
