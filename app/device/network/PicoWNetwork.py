import network
from app.device.network.BaseNetwork import BaseNetwork
from app.settings import NetworkSettings


class PicoWNetwork(BaseNetwork):
    wlan = None

    def __init__(self, settings: NetworkSettings):
        super().__init__(settings)
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.settings.ssid, self.settings.password)

    def is_connected(self) -> bool:
        return self.wlan.isconnected()
