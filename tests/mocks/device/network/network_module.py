STA_IF = 0


class WLAN:
    toggle = False
    connected = False

    def __init__(self, mode):
        pass

    def active(self, toggle: bool):
        self.toggle = toggle

    def connect(self, ssid, password):
        self.connected = True

    def isconnected(self):
        return self.toggle and self.connected
