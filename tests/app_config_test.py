from pathlib import Path

from cashflow.app_config import DEFAULT_CONFIG, AppConfig


def test_app_config_with_existing_file(tmp_path: Path) -> None:
    # Create a temporary config file with sample content

    config_file = tmp_path / "config.toml"
    config_file.write_text(DEFAULT_CONFIG)

    # Initialize AppConfig with the temporary file
    config = AppConfig(config_file)
    # Verify that the 'transactions' key was read correctly
    transactions = config.get("transactions")
    assert transactions is not None
    assert transactions.get("bankcsvpath") == "test_path"


def test_app_config_file_not_found(tmp_path: Path) -> None:
    # Use a path that does not exist
    config_file = tmp_path / "non_existent_config.toml"
    config = AppConfig(config_file)
    # AppConfig should have an empty config as file is missing
    assert config.config_data == {}
