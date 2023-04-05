import sys

from app.device import BaseNetwork
from tests.mocks.device.network.network_module import WLAN


class MockNetworkDriver(BaseNetwork):
    connected = False

    def connect(self):
        self.connected = True

    def is_connected(self) -> bool:
        return self.connected


def mock_network_wlan():
    try:
        del sys.modules['network']
    except KeyError:
        pass

    module = type(sys)('network_module')
    module.WLAN = WLAN
    module.STA_IF = 0
    sys.modules['network'] = module
