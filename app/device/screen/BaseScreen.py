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
        offset = 0
        self.load_page(page)

        for section in page.sections:
            section_width, _ = self.get_section_bounds(section)
            self.show_page_section(section, offset)
            if offset + section_width > self.attributes.width:
                page.is_animated = True
            offset += section_width + 1

    def show_page_section(self, section: PageSection, offset=0):
        if section.type == PageSectionType.TEXT:
            text, colour = section.contents
            self.show_text((offset, 0), text, colour)
        if section.type == PageSectionType.SPRITE:
            sprite_sheet, sheet_position = section.contents
            self.show_sprite(sprite_sheet, sheet_position, (offset, 0))

    def next_frame(self):
        if self.current_page is None:
            return None

        if self.current_page.is_animated:
            offset = 0
            for section in self.current_page.sections:
                section_width, _ = self.get_section_bounds(section)

                if offset + section_width > self.attributes.width:
                    if section_width - section.animation_frame < 0:
                        section.animation_frame = 0
                    self.show_page_section(section, offset - section.animation_frame)
                    section.animation_frame += 1
                offset += section_width

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
        raise NotImplementedError
