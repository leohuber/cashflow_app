from typing import TYPE_CHECKING

from pydantic import ValidationError
from rich.console import Console

from cashflow.app import CashFlowApp
from cashflow.app_config import AppConfig, load_config
from cashflow.app_paths import app_config_file

if TYPE_CHECKING:
    from pathlib import Path

console = Console()


def main() -> None:
    try:
        config_file: Path = app_config_file()
        config: AppConfig = load_config(config_file)
    except ValidationError as e:
        console.print(f"[red]Error loading config file: {e}[/]")
        return
    app = CashFlowApp(config=config)
    app.run()


if __name__ == "__main__":
    main()
