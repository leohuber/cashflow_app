from pathlib import Path

# The application data and config directories are stored in the user's home directory.
__config_home: Path = Path.home() / ".config"


def _cashflow_directory(root: Path) -> Path:
    directory: Path = root / "cashflow"
    directory.mkdir(exist_ok=True, parents=True)
    return directory


def config_directory() -> Path:
    """Return (possibly creating) the application config directory."""
    return _cashflow_directory(__config_home)


def app_config_file() -> Path:
    return config_directory() / "config.toml"
