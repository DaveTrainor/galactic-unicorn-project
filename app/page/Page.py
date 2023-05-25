class Page:
    is_animated: bool

    def __init__(self, sections=(), background: tuple[int, int, int] = (0, 0, 0)):
        self.background = background
        self.sections = sections
        self.is_animated = False

        for section in self.sections:
            section.page = self
