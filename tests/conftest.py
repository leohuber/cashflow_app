from __future__ import annotations

from collections.abc import Generator  # noqa: TC003
from typing import Any

import pytest
from sqlalchemy.orm import sessionmaker  # noqa: TC002

from cashflow.app_container import CashFlowContainer
from cashflow.data.db.entities import Base


@pytest.fixture
def container() -> Generator[CashFlowContainer, Any, Any]:
    # Configure the CashFlowContainer with the temporary database
    container = CashFlowContainer()
    container.cashflow_config().cashflow_db_file = ":memory:"

    # Create all tables
    Base.metadata.create_all(container.db_engine().engine)

    yield container

    # Cleanup after the test
    Base.metadata.drop_all(container.db_engine().engine)
    container.db_engine().engine.dispose()


@pytest.fixture
def session_maker(container: CashFlowContainer) -> sessionmaker:
    return container.db_engine().sessionmaker
