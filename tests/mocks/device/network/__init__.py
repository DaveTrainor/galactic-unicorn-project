import sys
import tests.mocks.device.network.network
from tests.mocks.device.network.network import MockNetworkDriver


def mock_network_device(mocker):
    available_devices = {
        'test': 'MockNetwork'
    }

    import app.device.network
    mocker.patch.dict(app.device.network.available_interfaces, available_devices)
    module = type(sys)('app.device.network.network.BaseNetwork')
    module.MockNetwork = MockNetworkDriver
    sys.modules['app.device.network.MockNetwork'] = module


def mock_import_with_mock_network(mocker):
    mock = mocker.patch('builtins.__import__')

    class Empty:
        pass

    app = Empty()
    app.device = Empty()
    app.device.network = Empty()
    app.device.network.MockNetwork = Empty()
    app.device.network.MockNetwork.MockNetwork = MockNetworkDriver
    mock.return_value = app

    return mock
