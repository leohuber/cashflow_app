from typing import ClassVar

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class CashFlowApp(App):
    """A console app to manage bank transactions and track expenses and income."""

    BINDINGS: ClassVar = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"
