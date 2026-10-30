from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Tree

from note_app.widgets import MarkdownWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%;
    }
    """
    BINDINGS = [("q", "quit", "Выход")]

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree(label="База знаний", id="tree")
            yield MarkdownWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"
        self.query_one(MarkdownWidget).text = "## Hello test"

    def action_quit(self):
        self.app.exit()
