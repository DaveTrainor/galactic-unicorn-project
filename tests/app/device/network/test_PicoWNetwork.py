from app.settings import NetworkSettings
from tests.mocks.device.network.network import mock_network_wlan


def test_connect(mocker):
    mock_network_wlan()
    from app.device.network.PicoWNetwork import PicoWNetwork
    settings = NetworkSettings()
    settings.driver = 'pico_w'
    settings.ssid = 'test_ssid'
    settings.password = 'test_password'
    network = PicoWNetwork(settings)
    active_spy = mocker.spy(network.wlan, 'active')
    connect_spy = mocker.spy(network.wlan, 'connect')
    isconnected_spy = mocker.spy(network.wlan, 'isconnected')
    assert False is network.is_connected()
    network.connect()
    active_spy.assert_called_with(True)
    connect_spy.assert_called_with('test_ssid', 'test_password')
    assert True is network.is_connected()
    isconnected_spy.assert_called()
