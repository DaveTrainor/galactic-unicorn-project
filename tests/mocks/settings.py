import sys


def tear_down():
    module = type(sys)('settings')
    sys.modules['settings'] = module


def full_settings():
    module = type(sys)('settings')
    module.screen = {
        'driver': 'test_screen_driver'
    }
    module.network = {
        'driver': 'test_network_driver',
        'ssid': 'test_network_ssid',
        'password': 'test_network_password',
    }
    sys.modules['settings'] = module


def screen_only_settings():
    module = type(sys)('settings')
    module.screen = {
        'driver': 'test_screen_driver'
    }
    sys.modules['settings'] = module


def no_module():
    module = type(sys)('settings')
    sys.modules['settings'] = module
