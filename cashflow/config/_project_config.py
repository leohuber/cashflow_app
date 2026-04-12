"""Configuration module for accessing pyproject.toml settings.

This module provides a centralized way to access configuration from pyproject.toml
and can be used throughout the application, including in env.py and app_paths.py.
"""

import tomllib
from pathlib import Path
from typing import Any


def find_pyproject_toml() -> Path:
    """Find the pyproject.toml file by traversing up from this module."""
    current_path = Path(__file__).resolve()

    # Traverse up the directory hierarchy recursively
    while current_path != current_path.parent:  # Stop at filesystem root
        config_path = current_path / "pyproject.toml"
        if config_path.exists():
            return config_path
        current_path = current_path.parent

    # If we reach here, pyproject.toml was not found
    raise FileNotFoundError("pyproject.toml")  # noqa: EM101


class _CashFlowProjectConfig:
    """Configuration reader for pyproject.toml."""

    def __init__(self) -> None:
        """Initialize the project configuration."""
        self._config_path: Path = find_pyproject_toml()
        with self._config_path.open("rb") as config_file:
            config: dict[str, Any] = tomllib.load(config_file)
            self._cashflow_home_dir: str = config.get("tool", {}).get("cashflow", {}).get("home-dir")
            self._alembic_script_location: str = config.get("tool", {}).get("alembic", {}).get("script_location")
            self._alembic_config: dict[str, Any] = config.get("tool", {}).get("alembic", {})

    def get_cashflow_home_dir(self) -> Path:
        """Get the CashFlow home directory configuration."""
        return Path.home() / self._cashflow_home_dir[2:] if self._cashflow_home_dir.startswith("~/") else Path(self._cashflow_home_dir)

    def get_alembic_script_location(self) -> Path:
        return Path(self._alembic_script_location)

    def get_alembic_config_items(self) -> dict[str, Any]:
        """Get all alembic configuration items from pyproject.toml."""
        return self._alembic_config.copy()
