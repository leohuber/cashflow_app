from typing import TYPE_CHECKING, Any

from cashflow.config._paths import _CashFlowPaths
from cashflow.config._project_config import _CashFlowProjectConfig
from cashflow.config._runtime_config import _CashFlowRuntimeConfig

if TYPE_CHECKING:
    from pathlib import Path


class CashFlowConfig:
    def __init__(self) -> None:
        self._project_config = _CashFlowProjectConfig()
        self._paths = _CashFlowPaths(self._project_config.get_cashflow_home_dir())
        self._runtime_config = _CashFlowRuntimeConfig(self._paths.get_cashflow_config_file())
        self._cashflow_db_file: str | None = None

    @property
    def cashflow_home_dir(self) -> Path:
        return self._project_config.get_cashflow_home_dir()

    @property
    def alembic_script_location(self) -> Path:
        return self._project_config.get_alembic_script_location()

    @property
    def cashflow_db_file(self) -> str:
        if self._cashflow_db_file is not None:
            return self._cashflow_db_file
        return str(self._paths.get_cashflow_db_file())

    @cashflow_db_file.setter
    def cashflow_db_file(self, db_file: str) -> None:
        self._cashflow_db_file = db_file

    @property
    def alembic_config_items(self) -> dict[str, Any]:
        return self._project_config.get_alembic_config_items()
