from sqlalchemy.orm import Session, sessionmaker  # noqa: TC002

from cashflow.data.db.data_access import BudgetDataAccess, CategoryDataAccess
from cashflow.data.db.entities import BudgetEntity, CategoryEntity


def _create_category(session: Session, name: str = "Food") -> CategoryEntity:
    category = CategoryEntity(name=name)
    CategoryDataAccess.save_category(session, category)
    return category


def test_get_all_budgets(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _create_category(session)
        budget1 = BudgetEntity(year=2024, limit=300.0, category_id=category.id)
        budget2 = BudgetEntity(year=2025, limit=500.0, category_id=category.id)
        BudgetDataAccess.save_budget(session, budget1)
        BudgetDataAccess.save_budget(session, budget2)
        session.commit()

        budgets = BudgetDataAccess.get_all_budgets(session)

        assert len(budgets) == 2
        assert any(b.id == budget1.id for b in budgets)
        assert any(b.id == budget2.id for b in budgets)


def test_get_budget_by_id(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _create_category(session)
        budget = BudgetEntity(year=2025, limit=250.0, category_id=category.id)
        BudgetDataAccess.save_budget(session, budget)
        session.commit()

        retrieved = BudgetDataAccess.get_budget_by_id(session, budget.id)

        assert retrieved is budget


def test_get_budget_by_id_not_found(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        result = BudgetDataAccess.get_budget_by_id(session, 9999)
        assert result is None


def test_save_budget_new(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _create_category(session)
        budget = BudgetEntity(year=2025, limit=400.0, category_id=category.id)

        saved = BudgetDataAccess.save_budget(session, budget)
        session.commit()

        assert saved.id is not None
        assert saved is budget


def test_save_budget_existing(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _create_category(session)
        budget = BudgetEntity(year=2025, limit=400.0, category_id=category.id)
        BudgetDataAccess.save_budget(session, budget)
        session.commit()

        budget.limit = 600.0
        updated = BudgetDataAccess.save_budget(session, budget)
        session.commit()

        retrieved = BudgetDataAccess.get_budget_by_id(session, updated.id)
        assert retrieved is not None
        assert retrieved.limit == 600.0


def test_delete_budget(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _create_category(session)
        budget = BudgetEntity(year=2025, limit=200.0, category_id=category.id)
        BudgetDataAccess.save_budget(session, budget)
        session.commit()

        budget_id = budget.id
        deleted = BudgetDataAccess.delete_budget(session, budget_id)
        session.commit()

        assert deleted is True
        assert BudgetDataAccess.get_budget_by_id(session, budget_id) is None


def test_delete_budget_not_found(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        result = BudgetDataAccess.delete_budget(session, 9999)
        assert result is False
