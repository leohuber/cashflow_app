---
description: "Use when adding or modifying DAO classes."
applyTo: "cashflow/data/db/data_access.py"
---

# Data Access Objects

- All DAOs live in `data_access.py` — one class per entity type.
- Name classes with the `DataAccess` suffix: e.g. `ContactDataAccess`, `MeetingDataAccess`.
- All methods are `@staticmethod` — no instance state.
- Every method receives a `Session` as first argument (injected by the caller, never created internally).
- For `save` operations:
  - New records (no `id`): use `session.add()` then `session.flush()` to populate the auto-generated ID.
  - Existing records (has `id`): use `session.merge()`.
- Session lifecycle (commit/rollback) is managed by the **service layer**, not DAOs.
- Import only entity classes (e.g. `ContactEntity`) from `entities.py` — no cross-layer imports.
