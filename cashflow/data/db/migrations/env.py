import logging
import sys
from typing import TYPE_CHECKING

from alembic import context

from cashflow.app_container import CashFlowContainer
from cashflow.data.db.entities import (
    Base,
    CategoryEntity,  # noqa: F401
    TransactionEntity,  # noqa: F401
)

if TYPE_CHECKING:
    from sqlalchemy import Engine

    from cashflow.config.config import CashFlowConfig
    from cashflow.data.db.db_engine import CashFlowDBEngine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Get CashFlow Config & DB Engine
container: CashFlowContainer = CashFlowContainer()
cashflow_config: CashFlowConfig = container.cashflow_config()
cashflow_db_engine: CashFlowDBEngine = container.db_engine()
engine: Engine = cashflow_db_engine.sqlalchemy_engine

# Update config with values from pyproject.toml
for key, value in cashflow_config.alembic_config_items.items():
    if key != "post_write_hooks":  # Skip post_write_hooks section
        config.set_main_option(key, str(value))

# Set up basic logging configuration since we're not using fileConfig
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-5.5s [%(name)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)

# Set specific logger levels
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("alembic").setLevel(logging.INFO)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    raise NotImplementedError("Offline migrations are not supported.")  # noqa: EM101


def run_migrations_online() -> None:
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
