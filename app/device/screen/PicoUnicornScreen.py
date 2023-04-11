import gc
from app.mods.msgpack_loads import loads
from .BaseScreen import BaseScreen, ScreenAttributes
from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK, PEN_RGB888

from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType
from ...settings import ScreenSettings


class PicoUnicornScreen(BaseScreen):
    attributes = ScreenAttributes(sprite_size=7, sprite_extension='bin', width=16, height=7)
    dimness = 10

    def __init__(self, settings: ScreenSettings):
        super().__init__(settings)
        self.sprite_sheet_pens = {}
        self.sprite_sheet = {}
        self.screen = PicoUnicorn()
        self.display = PicoGraphics(display=DISPLAY_UNICORN_PACK, pen_type=PEN_RGB888)
        self.display.set_font('bitmap6')

    def show_page(self, page: Page):
        offset = 0
        self.load_page(page)

        for section in page.sections:
            section_width, _ = self.get_section_bounds(section)
            self.show_page_section(section, offset)
            if offset + section_width > self.attributes.width:
                page.is_animated = True
            offset += section_width + 1

    def next_frame(self):
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

    def load_page(self, page: Page):
        sprites = {}
        self.current_page = page
        for section in page.sections:
            if section.type == PageSectionType.SPRITE:
                sprite_sheet, sheet_position = section.contents
                if sprites.get(sprite_sheet) is None:
                    sprites[sprite_sheet] = [sheet_position]
                else:
                    sprites[sprite_sheet].append(sheet_position)
        for name in sprites.keys():
            self.load_sprites(name, sprites[name])

    def show_page_section(self, section: PageSection, offset=0):
        if section.type == PageSectionType.TEXT:
            text, colour = section.contents
            self.show_text((offset, 0), text, colour)
        if section.type == PageSectionType.SPRITE:
            sprite_sheet, sheet_position = section.contents
            self.show_sprite(sprite_sheet, sheet_position, (offset, 0))

    def empty(self):
        self.sprite_sheet_pens = {}
        self.sprite_sheet = {}
        gc.collect()
        return self

    def set_dimness(self, dimness):
        self.dimness = dimness
        return self

    def colour_correction(self, colour):
        r, g, b = colour
        r = int((r * 2) / self.dimness)
        g = int(g / self.dimness)
        b = int(b / self.dimness / 2)
        return [r, g, b]

    def load_sprites(self, name, positions):
        with open(self.get_sprite_sheet_filename(name), "rb") as f:
            full_sprite_sheet = loads(f.read())
            sprite_sheet_size = full_sprite_sheet.get('d')
            if self.attributes.sprite_size != sprite_sheet_size:
                self.show_error(
                    f'sprite size for loaded sheet will not work with this display (display: ' +
                    f'{self.attributes.sprite_size}, sheet: {sprite_sheet_size})')
            for position in positions:
                start_sprite_x = position[0] * self.attributes.sprite_size
                start_sprite_y = position[1] * self.attributes.sprite_size
                sprite_rows = full_sprite_sheet.get('s')[start_sprite_x:start_sprite_x + self.attributes.sprite_size]
                sprite = []
                for row in sprite_rows:
                    sprite.append(row[start_sprite_y:start_sprite_y + self.attributes.sprite_size])
                self.sprite_sheet[tuple([name]) + position] = sprite

            for index, colour in enumerate(full_sprite_sheet.get('p')):
                colour = self.colour_correction(colour)
                self.sprite_sheet_pens[(name, index)] = self.display.create_pen(*colour)
            f.close()
        gc.collect()

        return self

    def get_sprite(self, sprite):
        return self.sprite_sheet[sprite]

    def show_text(self, position, text, colour=(100, 100, 100)):
        self.display.set_font('bitmap6')
        self.display.set_pen(self.display.create_pen(*self.colour_correction(colour)))
        self.display.text(text, position[0], position[1], scale=0.1)
        self.screen.update(self.display)
        return self

    def show_sprite(self, name, sprite, placement):
        sprite = self.sprite_sheet[tuple([name]) + sprite]
        for y in range(len(sprite)):
            if y > self.attributes.height - 1:
                continue
            for x in range(len(sprite[y])):
                if x > self.attributes.width - 1:
                    continue
                pixel = sprite[y][x]
                self.display.set_pen(self.sprite_sheet_pens[(name, pixel)])
                self.display.pixel(x + placement[0], y + placement[1])
        self.screen.update(self.display)
        return self
