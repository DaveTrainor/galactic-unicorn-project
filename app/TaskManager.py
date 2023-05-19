from app.settings import Settings
from app.tasks.BaseTask import BaseTask
from app.device import Devices


class TaskManager:
    _instance = None
    asyncio = None
    current_task: int
    devices: Devices
    settings: Settings
    tasks: list[BaseTask]
    input_fps = 15
    render_fps = 60
    state_fps = 60

    def __new__(cls, asyncio, devices: Devices, settings: Settings, tasks: list[BaseTask]):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.asyncio = asyncio
            cls._instance.devices = devices
            cls._instance.settings = settings
            cls._instance.tasks = tasks
            cls._instance.current_task = None
        return cls._instance

    def set_current_task(self, task_id: int):
        print(f'[taskmanager] switching to task {type(self.tasks[task_id])}')
        if self.current_task is not None:
            self.get_current_task().stop()
        self.devices.screen.clear()
        self.current_task = task_id
        self.get_current_task().start()

    def get_current_task(self) -> BaseTask:
        return self.tasks[self.current_task]

    async def input(self):
        while True:
            try:
                buttons = self.devices.screen.get_buttons()

                if buttons['right_2']:
                    if len(self.tasks) == self.current_task + 1:
                        self.set_current_task(0)
                    else:
                        self.set_current_task(self.current_task + 1)

                self.get_current_task().input(buttons)

                # If input received, hold for 200ms
                if any(buttons.values()):
                    await self.asyncio.sleep(0.2)

            except Exception as e:
                self.devices.screen.show_error(e)

            await self.asyncio.sleep(1.0 / self.input_fps)

    async def render(self):
        while True:
            try:
                self.get_current_task().render(self.devices.screen)
            except Exception as e:
                self.devices.screen.show_error(e)
            await self.asyncio.sleep(1.0 / self.render_fps)

    async def state(self):
        while True:
            try:
                self.get_current_task().state()
            except Exception as e:
                self.devices.screen.show_error(e)
            await self.asyncio.sleep(1.0 / self.state_fps)


def start_manager(asyncio, tasks: list[BaseTask], devices: Devices, settings: Settings):
    manager = TaskManager(asyncio, devices, settings, tasks)
    manager.set_current_task(0)

    async def task_manager_loop():
        print(f'[taskmanager] starting with tasks {[type(task) for task in tasks]}')
        asyncio.create_task(manager.input())
        asyncio.create_task(manager.render())
        asyncio.create_task(manager.state())
        while True:
            await asyncio.sleep(1)

    asyncio.run(task_manager_loop())
