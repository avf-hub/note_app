from typing import Optional

import html2text
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer

from note_app.config import AppSettings
from note_app.domain import Note
from note_app.repositories import FolderRepository, NoteRepository
from note_app.screens.import_modal import ImportModal
from note_app.widgets import NoteViewWidget, FileTreeWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%;
    }
    """
    BINDINGS = [
        ("q", "quit", "Выход"),
        ("i", "import", "Импорт"),
        ("d", "delete", "Удалить")
    ]

    def __init__(self, settings: AppSettings, folder_repo: FolderRepository, note_repo: NoteRepository, *args,
                 **kwargs):
        self.settings = settings
        self._folder_repo = folder_repo
        self._note_repo = note_repo
        self._dir = settings.data_directory
        self._note: Note | None = None
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield FileTreeWidget(self._folder_repo, self._note_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"

    def action_quit(self):
        self.app.exit()

    def action_delete(self):
        if self._note:
            self._note_repo.delete_note(self._note)
            self.query_one(FileTreeWidget).collapse()

    def action_import(self):
        self.app.push_screen(ImportModal(), self.handle_import)

    def handle_import(self, data: Optional[str]):
        if data:
            md = html2text.html2text(data)
            self._note_repo.create_note(self._dir, "imported", md)
            self.query_one(FileTreeWidget).collapse()

    def on_file_tree_widget_note_selected(self, message: FileTreeWidget.NoteSelected) -> None:
        note = self._note_repo.load_note(message.note_path)
        self._note = note
        if note.content:
            self.query_one(NoteViewWidget).text = note.content
        else:
            self.query_one(NoteViewWidget).text = ""

    def on_file_tree_widget_folder_selected(self, message: FileTreeWidget.FolderSelected) -> None:
        self._dir = message.folder_path
