from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from cashflow.config.config import CashFlowConfig
from cashflow.data.db.db_engine import CashFlowDBEngine
from cashflow.data.db.migration import Migration


class CashFlowContainer(DeclarativeContainer):
    cashflow_config: Singleton[CashFlowConfig] = Singleton(CashFlowConfig)

    db_engine: Singleton[CashFlowDBEngine] = Singleton(CashFlowDBEngine, db_file=cashflow_config.provided.cashflow_db_file)

    migration: Singleton[Migration] = Singleton(
        Migration,
        script_location=cashflow_config.provided.alembic_script_location,
    )


def build_container() -> CashFlowContainer:
    """Build the dependency injection container."""
    container = CashFlowContainer()

    # Initialize the database engine, can be removed if done in the CashFlowApp
    container.db_engine()

    return container


def wire_container(container: CashFlowContainer) -> None:
    """Wire the container with the necessary modules."""
    # container.wire(modules=["luna_app.view.contacts.widgets.contact_form"])  # noqa: ERA001
    # container.wire(modules=["luna_app.view.contacts.widgets.contact_list"])  # noqa: ERA001
    # container.wire(modules=["luna_app.view.contacts.contact_screen"])  # noqa: ERA001
