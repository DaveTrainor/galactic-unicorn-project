from .BaseScreen import BaseScreen
from app.settings import ScreenSettings

available_screens = {
}


def load_screen(settings: ScreenSettings) -> BaseScreen:
    driver = available_screens.get(settings.driver)
    mod = __import__(f'app.device.screen.{driver}')
    mod = getattr(mod.device.screen, driver)
    return getattr(mod, driver)(settings)
