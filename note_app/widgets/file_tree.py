from pathlib import Path

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Tree
from textual.widgets._tree import TreeNode

from note_app.domain import Folder
from note_app.repositories import BaseRepository


class FileTreeWidget(VerticalScroll):
    _tree: Tree

    def __init__(self, folder_repo: BaseRepository, *args, **kwargs):
        self._folder_repo = folder_repo
        super().__init__(*args, **kwargs)


    def compose(self) -> ComposeResult:
        self._tree = Tree("Заметки")
        yield self._tree

    def on_mount(self) -> None:
        root = self.query_one(Tree).root
        root.data = Folder("data", Path("data"))
        root.expand()

    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        node: TreeNode[Folder] = event.node
        node.remove_children()
        path = node.data.path if node.data else ""
        folders = self._folder_repo.get_folders_by_path(Path(path))
        for folder in folders:
            node.add(folder.name, folder)
