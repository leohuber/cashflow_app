from pathlib import Path

from cashflow.data.db.database import Category, DatabaseManager


def test_create_and_retrieve_category(tmp_path: Path) -> None:
    # Use a temporary file for the SQLite database
    db_path: Path = tmp_path / "test.db"
    db = DatabaseManager(db_path=db_path)
    db.create_tables()
    # Add a category
    category: Category = db.add_category(name="Food", description="Groceries and dining out")
    assert category.id is not None
    assert category.name == "Food"
    # Retrieve all categories
    categories = db.get_all_categories()
    assert len(categories) == 1
    assert categories[0].name == "Food"
    assert categories[0].description == "Groceries and dining out"
