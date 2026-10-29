from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer


class MainScreen(Screen):
    BINDINGS = [("q", "quit", "Выход")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"

    def action_quit(self):
        self.app.exit()
