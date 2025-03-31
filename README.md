[![Actions status](https://github.com/leohuber/cashflow_app/actions/workflows/cashflow-main-build.yml/badge.svg)](https://github.com/leohuber/cashflow_app/actions)


# Cashflow

## Development Setup

### Setting Up the Python Environment

To initialize the Python environment using the `uv` tool, follow these steps:

1. **Install `rustc`, `cargo` and `rustup`**: Install (if not done already) the standalone installer from [https://www.rust-lang.org](https://www.rust-lang.org/tools/install)

2. **Install `uv`**: Install (if not done already) the standalone installer from [https://docs.astral.sh](https://docs.astral.sh/uv/getting-started/installation/)

3. **Initialize or Syncronize the environment**:
    ```sh
    uv sync
    ```

4. **Run the application**:
    ```sh
    uv run cashflow
    ```

These commands will set up and activate a new Python environment using `uv`.

## Install pre-commit

1. **Install the git hook scripts**:
    ```bash
    uv run pre-commit install
    ```

2. **Run pre-commit on all files**:
    ```bash
    uv run pre-commit run --all-files
    ```
