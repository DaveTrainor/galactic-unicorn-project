import builtins
from importlib import reload
import tests.mocks.settings as mock_settings
import app.settings
import pytest


def test_full_settings_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.full_settings()
    reload(app.settings)
    settings = app.settings.Settings()

    assert 'test_screen_driver' == settings.screen.driver
    assert 'test_network_driver' == settings.network.driver
    assert 'test_network_ssid' == settings.network.ssid
    assert 'test_network_password' == settings.network.password
    assert (10.20, 20.50) == settings.locale.coordinates
    assert 'Europe/London' == settings.locale.timezone

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] loaded')
    print_mock.assert_any_call('[settings.network.driver] loaded')
    print_mock.assert_any_call('[settings.network.ssid] loaded')
    print_mock.assert_any_call('[settings.network.password] loaded')
    print_mock.assert_any_call('[settings.locale.coordinates] loaded')
    print_mock.assert_any_call('[settings.locale.timezone] loaded')


def test_screen_only_settings_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.screen_only_settings()
    reload(app.settings)
    settings = app.settings.Settings()

    assert 'test_screen_driver' == settings.screen.driver
    assert None is settings.network.driver
    assert None is settings.network.ssid
    assert None is settings.network.password
    assert None is settings.locale.coordinates
    assert None is settings.locale.timezone

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] loaded')
    print_mock.assert_any_call('[settings.network.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.ssid] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.password] did not find value in settings.py')
    print_mock.assert_any_call('[settings.locale.coordinates] did not find value in settings.py')
    print_mock.assert_any_call('[settings.locale.timezone] did not find value in settings.py')



def test_no_settings_in_file(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.no_settings_in_file()
    reload(app.settings)
    settings = app.settings.Settings()

    assert None is settings.screen.driver
    assert None is settings.network.driver
    assert None is settings.network.ssid
    assert None is settings.network.password
    assert None is settings.locale.coordinates
    assert None is settings.locale.timezone

    print_mock.assert_any_call('[settings] loading device settings')
    print_mock.assert_any_call('[settings.screen.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.driver] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.ssid] did not find value in settings.py')
    print_mock.assert_any_call('[settings.network.password] did not find value in settings.py')
    print_mock.assert_any_call('[settings.locale.coordinates] did not find value in settings.py')
    print_mock.assert_any_call('[settings.locale.timezone] did not find value in settings.py')


def test_no_settings_file(mocker):
    stop_mock = mock_settings.no_settings_file(mocker)
    reload(app.settings)
    with pytest.raises(Exception) as e:
        settings = app.settings.Settings()
        assert None is settings.screen.driver
        assert None is settings.network.driver
        assert None is settings.network.ssid
        assert None is settings.network.password
        assert None is settings.locale.coordinates
        assert None is settings.locale.timezone
        assert str(e.value) == 'Cannot load settings, check settings.py'

    stop_mock()
