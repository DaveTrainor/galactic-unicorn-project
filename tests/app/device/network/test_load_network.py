from app.settings import NetworkSettings
from tests.mocks.device.network import mock_network_device, mock_import_with_mock_network, MockNetworkDriver


def test_loading_a_test_network_interface(mocker):
    mock_network_device(mocker)
    from app.device.network import load_network
    import_mock = mock_import_with_mock_network(mocker)
    settings = NetworkSettings()
    settings.driver = 'test'
    network = load_network(settings)

    assert isinstance(network, MockNetworkDriver)
    import_mock.assert_called_with('app.device.network.MockNetwork')
    import_mock.stop()
