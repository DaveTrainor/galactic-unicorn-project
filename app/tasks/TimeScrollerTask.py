from .BaseTask import BaseTask
from app.clients.TimeClient import TimeClient
from app.page.Page import Page
from app.page.PageSection import PageSection, PageSectionType


class TimeScrollerTask(BaseTask):
    page: Page
    counter: int

    def __init__(self, settings):
        super().__init__(settings)
        self.counter = 0
        self.page = Page([
            PageSection(PageSectionType.TEXT, ('loading', (0, 255, 0))),
        ], (100, 0, 0))

    def start(self):
        self._load_time()

    def stop(self):
        pass

    def input(self, buttons):
        pass

    def state(self):
        self.counter += 1

        if self.counter > 6000:
            self._load_time()
            self.counter = 0

    def render(self, screen):
        if self.counter == 0:
            screen.show_page(self.page)
        if self.counter % 10 == 0:
            screen.next_frame()

    def _load_time(self):
        self.page = Page([
            PageSection(PageSectionType.TEXT, (TimeClient().get_time(self.settings.locale), (0, 255, 0))),
        ], (100, 0, 0))
