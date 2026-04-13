from sqlalchemy.orm import sessionmaker  # noqa: TC002

from cashflow.data.db.data_access import CategoryDataAccess
from cashflow.data.db.entities import CategoryEntity


def test_get_all_categories(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        new_category1: CategoryEntity = CategoryEntity(name="Category 1")
        new_category2: CategoryEntity = CategoryEntity(name="Category 2")
        new_category3: CategoryEntity = CategoryEntity(name="Category 3")
        new_category4: CategoryEntity = CategoryEntity(name="Category 4")
        new_category5: CategoryEntity = CategoryEntity(name="Category 5")

        CategoryDataAccess.save_category(session, new_category1)
        CategoryDataAccess.save_category(session, new_category2)
        CategoryDataAccess.save_category(session, new_category3)
        CategoryDataAccess.save_category(session, new_category4)
        CategoryDataAccess.save_category(session, new_category5)
        session.commit()

        # Retrieve all categories
        categories: list[CategoryEntity] = CategoryDataAccess.get_all_categories(session)

        # Check if the added categories are in the list
        assert len(categories) == 5
        assert any(c.id == new_category1.id for c in categories)
        assert any(c.id == new_category2.id for c in categories)
        assert any(c.id == new_category3.id for c in categories)
        assert any(c.id == new_category4.id for c in categories)
        assert any(c.id == new_category5.id for c in categories)


def test_get_category_by_id(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        # Create and save a category
        new_category: CategoryEntity = CategoryEntity(name="Category 1")
        CategoryDataAccess.save_category(session, new_category)
        session.commit()

        # Retrieve the category by ID
        retrieved_category: CategoryEntity | None = CategoryDataAccess.get_category_by_id(session, new_category.id)

        # Check if the retrieved category matches the added category (should be same instance due to same session)
        assert retrieved_category is new_category
