from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Tree

from note_app.repositories import BaseRepository


class FileTreeWidget(VerticalScroll):
    _tree: Tree

    def __init__(self, folder_repo: BaseRepository, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self._folder_repo = folder_repo


    def compose(self) -> ComposeResult:
        self._tree = Tree("Заметки")
        return self._tree
