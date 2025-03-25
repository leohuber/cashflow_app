from pathlib import Path

import pytest
from pydantic import ValidationError

from cashflow import app_config
from cashflow.app_config import AppConfig, load_config


def test_app_config(tmp_path: Path) -> None:
    # Create a temporary config file with sample content

    config_file: Path = tmp_path / "config.toml"
    config: AppConfig = load_config(config_file)
    assert config.data_path == Path.home()


def test_app_config_path_not_existent(tmp_path: Path) -> None:
    # Create a temporary config file with sample content

    app_config.__default_config = """
account_tx_csv_path = "some_path_that_does_not_exist"
"""  # noqa: SLF001

    config_file: Path = tmp_path / "config.toml"
    with pytest.raises(ValidationError):
        load_config(config_file)
