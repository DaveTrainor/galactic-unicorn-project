from app.device.network.BaseNetwork import BaseNetwork
from app.settings import NetworkSettings

available_interfaces = {
    'pico_w': 'PicoWNetwork',
}


def load_network(settings: NetworkSettings) -> BaseNetwork:
    driver = available_interfaces.get(settings.driver)
    mod = __import__(f'app.device.network.{driver}')
    mod = getattr(mod.device.network, driver)
    return getattr(mod, driver)(settings)
