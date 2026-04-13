---
description: "Use when adding or modifying SQLAlchemy ORM entity classes in entities.py. Covers entity naming, column declarations, enum placement, repr, and Base inheritance conventions."
applyTo: "cashflow/data/db/entities.py"
---

# Entity Classes

- All ORM models live in `entities.py` — never split entities across multiple files.
- Inherit from `Base` (the shared `DeclarativeBase` subclass defined at the top of `entities.py`).
- Use `Mapped[T]` and `mapped_column(...)` for all columns (SQLAlchemy 2.x style).
- Name classes with the `Entity` suffix: e.g. `ContactEntity`, `MeetingEntity`.
- Name tables in snake_case, plural or singular — consistent with existing tables.
- Define `__repr__` for every entity for debuggability.
- Use `deferred=False` explicitly for columns that are always needed.
- Enum types: define them as `enum.Enum` subclasses in `entities.py` — do NOT put enums elsewhere.
