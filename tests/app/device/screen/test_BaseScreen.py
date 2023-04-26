from app.device.screen.BaseScreen import BaseScreen, ScreenAttributes
from app.settings import ScreenSettings


class MockScreen(BaseScreen):
    attributes = ScreenAttributes(8, 'test', 20, 20)


def test_base_screen_get_sprite_sheet_filename():
    settings = ScreenSettings()
    screen = MockScreen(settings)

    assert 'app/sprites/sheet.test' == screen.get_sprite_sheet_filename('sheet')
