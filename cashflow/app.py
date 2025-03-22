from typing import ClassVar

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from cashflow.screens.modalscreen import ModalScreen


class CashFlowApp(App):
    """A console app to manage bank transactions and track expenses and income."""

    BINDINGS: ClassVar = [("d", "toggle_dark", "Toggle dark mode"), ("b", "push_screen('no_csv_data_error')", "BSOD")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.install_screen(ModalScreen("No CSV Data Available"), name="no_csv_data_error")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"
