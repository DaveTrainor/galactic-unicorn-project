from app.settings import ScreenSettings
from tests.mocks.device.screen import MockScreen, mock_screen_device, mock_import_with_mock_screen


def test_loading_a_test_screen(mocker):
    mock_screen_device(mocker)
    from app.device.screen import load_screen
    import_mock = mock_import_with_mock_screen(mocker)
    settings = ScreenSettings()
    settings.driver = 'test'
    screen = load_screen(settings)

    assert isinstance(screen, MockScreen)
    import_mock.assert_called_with('app.device.screen.MockScreen')
    import_mock.stop()
