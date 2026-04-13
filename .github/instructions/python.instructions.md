---
description: "Use when adding, modifying, deleting, or refactoring code in cashflow Python files. Covers emoji markers for change type annotation."
applyTo: "cashflow/**/*.py, tessts/**/*.py"
---

# Python Development Instructions

- This repository is a Python project. Prefer Python-specific tooling, conventions, and standard library solutions unless the existing codebase clearly uses something else.
- Use `uv` for Python dependency management, environment management, and command execution.
- Do not use bare `python`, `pip`, `pytest`, or similar commands when `uv` can run the same workflow.
