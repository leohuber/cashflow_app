import pandas as pd
from pandas import DataFrame
from textual.widgets import DataTable


class DataFrameTable(DataTable):
    """Display Pandas dataframe in DataTable widget."""

    DEFAULT_CSS = """
    DataFrameTable {
        height: 1fr
    }
    """

    def add_df(self, df: DataFrame) -> "DataFrameTable":
        """Add DataFrame data to DataTable."""
        self.df: DataFrame = df
        self.add_columns(*df.columns)
        self.add_rows(df.itertuples(index=False, name=None))
        return self

    def update_df(self, df: pd.DataFrame) -> None:
        """Update DataFrameTable with a new DataFrame."""
        self.clear(columns=True)
        self.add_df(df)
