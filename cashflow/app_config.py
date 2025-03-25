import tomllib as toml
from pathlib import Path
from typing import Any

from pydantic import BaseModel, DirectoryPath

__default_config = f"""# Data path to the cashflow data directory contianing the CSV files and other data
data_path = "{Path.home()}"
"""


class AppConfig(BaseModel):
    data_path: DirectoryPath


def load_config(config_file: Path) -> AppConfig:
    if not config_file.exists():
        with config_file.open("w") as file:
            file.write(__default_config)
    with config_file.open() as file:
        config: dict[str, Any] = toml.loads(file.read())
    return AppConfig(**config)
