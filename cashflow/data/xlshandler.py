from pathlib import Path

import pandas as pd
from pandas import DataFrame


def load_excel_file(xls_path: Path) -> DataFrame:
    return pd.read_excel(xls_path)
