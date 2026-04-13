---
description: "Use when adding or modifying entity classes tests."
applyTo: "tests/data/db/entities/**"
---

# Entity Classes Tests

- One file per entity (e.g. `category_entity_test.py`, `transaction_entity_test.py`).
- Test ORM constraints (e.g. non-nullable fields, relationships) by attempting to create entities with invalid data and asserting that exceptions are raised.
- Test `__repr__` returns a string containing the class name and key attributes.
- If a test does not exist for an existing entity, create it.