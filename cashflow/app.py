from typing import TYPE_CHECKING, ClassVar

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.widgets import Footer, Header

from cashflow.app_config import AppConfig
from cashflow.data.csvhandler import list_csv_files, load_dataframe
from cashflow.screens.modalscreen import ModalScreen
from cashflow.widgets.dataframetable import DataFrameTable

if TYPE_CHECKING:
    from pathlib import Path

    from pandas import DataFrame


class CashFlowApp(App):
    """A console app to manage and analyze expenses and income."""

    BINDINGS: ClassVar[list[BindingType]] = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("b", "push_screen('no_csv_data_error')", "No CSV Data Error"),
        ("q", "app.quit", "Quit the app"),
    ]

    def __init__(self, config: AppConfig) -> None:
        super().__init__()
        self.config: AppConfig = config
        self.title = "CashFlow"
        self.sub_title = "Manage and analyze expenses and income"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield DataFrameTable()
        yield Footer()

    def on_mount(self) -> None:
        self.install_screen(ModalScreen("No CSV Data Available"), name="no_csv_data_error")
        csv_files: list[Path] = list_csv_files(self.config.data_path)
        transactions: DataFrame = load_dataframe(csv_files[0])
        table: DataFrameTable = self.query_one(DataFrameTable)
        table.add_df(transactions)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"
