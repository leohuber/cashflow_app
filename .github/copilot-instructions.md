

# Required Command Patterns

- Install or sync dependencies with `uv sync`.
- Add runtime dependencies with `uv add <package>`.
- Add development dependencies with `uv add --dev <package>`.
- Remove dependencies with `uv remove <package>`.
- Run the application or scripts with `uv run <command>`.
- Run tests with `uv run pytest`.
- Run one-off Python checks or scripts with `uv run python <script>` or `uv run python -c "..."`.

# Linting And Code Quality

- Ruff rules are strict in this repository and must be followed.
- Before finishing Python changes, run `uv run ruff check .` and fix all reported violations in the files you changed.
- Do not bypass Ruff with unnecessary `noqa`, blanket ignores, or rule suppressions unless the user explicitly asks for that tradeoff.
- Keep code compatible with the repository Ruff configuration in `pyproject.toml`, including the enabled `ALL` rule set and existing per-file exceptions.
- Prefer code changes that satisfy Ruff cleanly over narrowly silencing warnings.

# Testing And Validation

- After Python code changes, run the smallest relevant validation first, then broader checks if needed.
- For tests, prefer targeted invocations such as `uv run pytest tests/path_to_test.py` before running the full suite.
- If you add or change behavior, update or add tests when the repository already has a suitable test location.

# Implementation Expectations

- Preserve existing project style and structure.
- Add type hints where they improve clarity and align with surrounding code.
- Keep changes minimal, focused, and consistent with current architecture.