from pathlib import Path

import click
from pydantic import ValidationError
from rich.console import Console

from cashflow.app import CashFlowApp
from cashflow.app_config import AppConfig, load_config
from cashflow.app_paths import app_config_file

console = Console()


@click.command()
@click.option(
    "--config",
    type=click.Path(dir_okay=False),
    default=app_config_file(),
    help="Path to the configuration file.",
)
def main(config: str) -> None:
    try:
        app_config: AppConfig = load_config(Path(config))
    except ValidationError as e:
        console.print(f"[red]Error loading config file: {e}[/]")
        return
    app = CashFlowApp(config=app_config)
    app.run()


if __name__ == "__main__":
    main()
