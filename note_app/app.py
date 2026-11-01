from .config import AppSettings
from .screens import MainScreen
from textual.app import App


class NoteManagerApp(App):
    def __init__(self, settings: AppSettings, *args, **kwargs):
        self.settings = settings
        super().__init__(*args, **kwargs)

    def on_mount(self):
        main_screen = MainScreen(self.settings)
        self.push_screen(main_screen)
