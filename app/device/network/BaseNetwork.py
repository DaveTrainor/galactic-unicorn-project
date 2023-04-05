from app.settings import NetworkSettings


class BaseNetwork:
    settings: NetworkSettings

    def __init__(self, network_settings: NetworkSettings):
        self.settings = network_settings

    def connect(self):
        raise NotImplementedError

    def is_connected(self) -> bool:
        raise NotImplementedError
