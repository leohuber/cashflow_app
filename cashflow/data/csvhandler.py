from pathlib import Path

import pandas as pd
from pandas import DataFrame


def list_csv_files(data_path: Path) -> list[Path]:
    if not data_path.is_dir():
        return []
    csv_dir = data_path / "csv_import"
    csv_dir.mkdir(parents=True, exist_ok=True)
    return list(csv_dir.rglob("*.csv"))


def load_dataframe(csv_path: Path) -> DataFrame:
    with csv_path.open() as file:
        return pd.read_csv(file, skiprows=9, delimiter=";")
