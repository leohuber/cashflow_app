from pathlib import Path
from typing import Any

import yaml


class _CashFlowRuntimeConfig:
    def __init__(self, config_file_path: Path) -> None:
        if not config_file_path.exists():
            default_file = Path(__file__).parent / "default.yml"
            config_file_path.write_text(default_file.read_text())

        self.config: dict[str, Any] = yaml.safe_load(config_file_path.read_text())
