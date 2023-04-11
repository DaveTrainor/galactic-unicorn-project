from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType
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

    def get_section_bounds(self, section: PageSection) -> (int, int):
        if section.type == PageSectionType.SPRITE:
            return self.attributes.sprite_size, self.attributes.sprite_size
        if section.type == PageSectionType.TEXT:
            text, _ = section.contents
            return self.display.measure_text(text, 1), self.attributes.height

    def show_page(self, page: Page):
        raise NotImplemented

    def next_frame(self):
        raise NotImplemented

    def clear(self, bounding=None, colour=(0, 0, 0)):
        self.display.set_pen(self.display.create_pen(*self.colour_correction(colour)))

        if bounding is None:
            self.display.clear()
        else:
            ((x, y), (width, height)) = bounding
            self.display.rectangle(x, y, width, height)

        self.screen.update(self.display)
        return self

    def show_error(self, message):
        self.clear()
        self.clear(((0, 0), (1, 1)), (255, 0, 0))
        self.clear(((self.attributes.width - 1, self.attributes.height - 1), (1, 1)), (255, 0, 0))
        raise Exception(message)

    def colour_correction(self, colour):
        raise NotImplemented
