"""Database migration service for Luna app."""

from typing import TYPE_CHECKING

from alembic import command
from alembic.config import Config
from rich.console import Console
from sqlalchemy.exc import SQLAlchemyError

if TYPE_CHECKING:
    from pathlib import Path

console = Console()


class Migration:
    """Service for handling database migrations using Alembic."""

    def __init__(self, script_location: Path) -> None:
        """Initialize the migration service.

        Args:
            script_location: Path to the Alembic migration scripts directory
        """
        self.__alembic_cfg: Config = Config()
        self.__alembic_cfg.set_main_option("script_location", str(script_location))

    def migrate_to_latest(self) -> bool:
        """Migrate database to the latest revision.

        Returns:
            True if migration was successful, False otherwise
        """
        try:
            command.upgrade(self.__alembic_cfg, "head")
        except SQLAlchemyError as e:
            console.print(f"[bold red]Migration failed:[/bold red] {e}")
            return False
        else:
            return True
