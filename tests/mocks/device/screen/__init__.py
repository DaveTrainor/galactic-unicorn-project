import sys
import tests.mocks.device.screen.screen
from tests.mocks.device.screen.screen import MockScreen


def mock_screen_device(mocker):
    available_devices = {
        'test': 'MockScreen'
    }

    import app.device.network
    mocker.patch.dict(app.device.screen.available_screens, available_devices)
    module = type(sys)('app.device.screen.screen.BaseScreen')
    module.MockScreen = MockScreen
    sys.modules['app.device.screen.MockScreen'] = module


def mock_import_with_mock_screen(mocker):
    mock = mocker.patch('builtins.__import__')

    class Empty:
        pass

    app = Empty()
    app.device = Empty()
    app.device.screen = Empty()
    app.device.screen.MockScreen = Empty()
    app.device.screen.MockScreen.MockScreen = MockScreen
    mock.return_value = app

    return mock
