from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class _CashFlowPaths:
    """Class for managing CashFlow application paths and directories."""

    def __init__(self, homedir: Path) -> None:
        """Initialize the CashFlowPaths instance with home directory."""
        self._home_dir: Path = homedir

    def _cashflow_directory(self, root: Path) -> Path:
        """Create and return a cashflow subdirectory within the given root path."""
        directory: Path = root / "cashflow"
        directory.mkdir(exist_ok=True, parents=True)
        return directory

    def _data_directory(self) -> Path:
        """Return (possibly creating) the application data directory."""
        data_home: Path = self._home_dir / ".local" / "share"
        return self._cashflow_directory(data_home)

    def _config_directory(self) -> Path:
        """Return (possibly creating) the application config directory."""
        config_home: Path = self._home_dir / ".config"
        return self._cashflow_directory(config_home)

    def get_cashflow_config_file(self) -> Path:
        """Return the path to the application config file."""
        return self._config_directory() / "config.yml"

    def get_cashflow_db_file(self) -> Path:
        """Return the path to the application database file."""
        return self._data_directory() / "cashflow_sqlite.db"
