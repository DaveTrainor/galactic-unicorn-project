import builtins
from importlib import reload
import tests.mocks.settings as mock_settings
import app.settings


def test_full_settings_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.full_settings()
    reload(app.settings)
    settings = app.settings.Settings()

    assert 'test_screen_driver' == settings.screen.driver
    assert 'test_network_driver' == settings.network.driver
    assert 'test_network_ssid' == settings.network.ssid
    assert 'test_network_password' == settings.network.password

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] loaded')
    print_mock.assert_any_call('[settings.network.driver] loaded')
    print_mock.assert_any_call('[settings.network.ssid] loaded')
    print_mock.assert_any_call('[settings.network.password] loaded')


def test_screen_only_settings_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.screen_only_settings()
    reload(app.settings)
    settings = app.settings.Settings()

    assert 'test_screen_driver' == settings.screen.driver
    assert None is settings.network.driver
    assert None is settings.network.ssid
    assert None is settings.network.password

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] loaded')
    print_mock.assert_any_call('[settings.network.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.ssid] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.password] did not find value in settings.py')


def test_no_existing_settings_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.no_module()
    reload(app.settings)
    settings = app.settings.Settings()

    assert None is settings.screen.driver
    assert None is settings.network.driver
    assert None is settings.network.ssid
    assert None is settings.network.password

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.ssid] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.password] did not find value in settings.py')
