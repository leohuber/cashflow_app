from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static


class ModalScreen(Screen):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        yield Static(" Windows ", id="title")
        yield Static(self.message, id="message")
