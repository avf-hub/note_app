from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer

from note_app.config import AppSettings
from note_app.repositories import FolderRepository
from note_app.widgets import NoteViewWidget, FileTreeWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%;
    }
    """
    BINDINGS = [("q", "quit", "Выход")]

    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = settings

    def compose(self) -> ComposeResult:
        folder_repo = FolderRepository(self.settings.data_directory)
        yield Header()
        with Horizontal():
            yield FileTreeWidget(folder_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"
        self.query_one(NoteViewWidget).text = "## Hello test"

    def action_quit(self):
        self.app.exit()
