from app.device.screen import BaseScreen
from app.settings import Settings


class BaseTask:
    def __init__(self, settings: Settings):
        self.settings = settings

    def start(self):
        """Run when a task is activated, use for task setup or optional reinitialisation
        """
        raise NotImplementedError

    def stop(self):
        """Run when a task is deactivated, use to unload parts of the task that use a lot of ram (pages with sprites)
        """
        raise NotImplementedError

    def input(self, buttons):
        """Ran at regular intervals, this method should alter the state of the task based on input buttons

        Parameters
        ----------
        buttons : dict[bool]
            A dictionary of buttons (taken from the loaded screen driver) with boolean to show if pressed
        """
        raise NotImplementedError

    def state(self):
        """Ran at regular intervals, this method should alter the state of the task based on the passage of time
        """
        raise NotImplementedError

    def render(self, screen: BaseScreen):
        """Ran at regular intervals, this task should update the screen based on the current state of the task

        Parameters
        ----------
        screen : BaseScreen
            The screen driver loaded based on settings.py
        """
        raise NotImplementedError
