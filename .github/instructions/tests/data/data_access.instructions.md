---
description: "Use when adding or modifying DAO classes tests."
applyTo: "tests/data/db/data_access/**"
---

# DAO Tests

- One file per DAO class (e.g. `category_data_access_test.py`, `transaction_data_access_test.py`).
- Use fixtures to set up test data in the database before each test.
- Test all CRUD operations: `get_all`, `get_by_id`, `save`, and `delete` (if applicable).
- Assert that the database state changes as expected after each operation (e.g. new record is created, existing record is updated, record is deleted).
- If a test does not exist for an existing DAO, create it.