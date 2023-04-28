import builtins
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
    module.locale = {
        'coordinates': (10.20, 20.50),
        'timezone': 'Europe/London'
    }
    sys.modules['settings'] = module


def screen_only_settings():
    module = type(sys)('settings')
    module.screen = {
        'driver': 'test_screen_driver'
    }
    sys.modules['settings'] = module


def no_settings_in_file():
    module = type(sys)('settings')
    sys.modules['settings'] = module


def no_settings_file(mocker):
    import builtins
    real_import = builtins.__import__

    def myimport(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'settings':
            raise ImportError
        return real_import(name, globals, locals, fromlist, level)

    builtins.__import__ = myimport

    def stop():
        builtins.__import__ = real_import

    return stop
