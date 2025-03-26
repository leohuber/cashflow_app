from typing import Any, ClassVar

import pandas as pd
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from cashflow.app_config import AppConfig
from cashflow.screens.modalscreen import ModalScreen
from cashflow.widgets.dataframetable import DataFrameTable

# Pandas DataFrame
dataframe: Any = pd.DataFrame()
dataframe["Name"] = ["Dan", "Ben", "Don", "John", "Jim", "Harry"]
dataframe["Score"] = [77, 56, 90, 99, 83, 69]
dataframe["Grade"] = ["C", "F", "A", "A", "B", "D"]


class CashFlowApp(App):
    """A console app to manage and analyze expenses and income."""

    BINDINGS: ClassVar = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("b", "push_screen('no_csv_data_error')", "BSOD"),
        ("q", "app.quit", "Quit the app"),
    ]

    def __init__(self, config: AppConfig | None) -> None:
        super().__init__()
        self.config: AppConfig | None = config
        self.title = "CashFlow"
        self.sub_title = "Manage and analyze expenses and income"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield DataFrameTable()
        yield Footer()

    def on_mount(self) -> None:
        self.install_screen(ModalScreen("No CSV Data Available"), name="no_csv_data_error")
        table = self.query_one(DataFrameTable)
        table.add_df(dataframe)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"
