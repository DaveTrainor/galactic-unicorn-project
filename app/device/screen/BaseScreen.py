from app.settings import ScreenSettings


class ScreenAttributes:
    def __init__(self, sprite_size, sprite_extension, width, height):
        self.sprite_size = sprite_size
        self.sprite_extension = sprite_extension
        self.width = width
        self.height = height


class BaseScreen:
    attributes: ScreenAttributes
    screen = None
    display = None
    current_page = None

    def __init__(self, settings: ScreenSettings):
        pass

    def get_sprite_sheet_filename(self, name):
        return f'app/sprites/{name}.{self.attributes.sprite_extension}'
