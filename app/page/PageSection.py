class PageSectionType:
    TEXT = 1
    SPRITE = 2


class PageSection:
    def __init__(self, section_type: int, contents):
        self.type = section_type
        self.contents = contents
        self.animation_frame = 0
