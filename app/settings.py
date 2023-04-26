class ScreenSettings:
    driver: str = None


class NetworkSettings:
    driver: str = None
    ssid: str = None
    password: str = None
    

class LocaleSettings:
    coordinates: tuple[float, float] = None
    
    
class Settings:
    screen = ScreenSettings()
    network = NetworkSettings()
    locale = LocaleSettings()

    def __init__(self):
        print('[settings] loading device settings')
        try:
            import settings
            self.__settings = settings
        except ImportError:
            raise SettingsLoadError('No settings.py file, please create one.')

        self.__attempt_load('screen', 'driver')
        self.__attempt_load('network', 'driver')
        self.__attempt_load('network', 'ssid')
        self.__attempt_load('network', 'password')
        self.__attempt_load('locale', 'coordinates')

    def __attempt_load(self, setting_block, setting_property):
        try:
            setting = getattr(self, setting_block)
            setattr(setting, setting_property, getattr(self.__settings, setting_block).get(setting_property))
            print(f'[settings.{setting_block}.{setting_property}] loaded')
        except AttributeError:
            print(f'[settings.{setting_block}.{setting_property}] did not find value in settings.py')


class SettingsLoadError(Exception):
    def __init__(self, setting=None):
        super().__init__('Cannot load settings, check settings.py')
