import tomllib as toml
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = """
[paths]
bankcsvpath= "path_to_csv_directory"
"""


class AppConfig:
    def __init__(self, config_file: Path) -> None:
        self.config_file: Path = config_file
        self.config_data: dict[str, Any] = self._read_config()

    def _read_config(self) -> dict[str, str]:
        try:
            with self.config_file.open() as file:
                return toml.loads(file.read())
        except FileNotFoundError:
            return {}

    def get(self, key: str, default: Any = None) -> Any:  # noqa: ANN401
        return self.config_data.get(key, default)
