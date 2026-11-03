from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Static, Input, Button


class ImportModal(ModalScreen):
    CSS = """
        Screen {
            align: center middle;
        }
        
        #dialog {
            width: 60;
            height: 15;
            border: solid grey;
        }
        
        #title {
            dock: top;
            height: 2;
            content-align: center middle;
            padding: 0 1;
        }
        
        #buttons {
            align: center middle;
        }
    """

    def compose(self) -> ComposeResult:
        with Container(id="dialog"):
            yield Static("Импорт данных", id="title")
            yield Input(placeholder="Введите url для импорта")
            with Horizontal(id="buttons"):
                yield Button(label="Импортировать", variant="primary")
                yield Button("Отмена")
