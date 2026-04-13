import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker  # noqa: TC002

from cashflow.data.db.entities import BudgetEntity, CategoryEntity


def _make_category(session: Session, name: str = "Food") -> CategoryEntity:
    category = CategoryEntity(name=name)
    session.add(category)
    session.flush()
    return category


def test_budget_entity_repr(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _make_category(session)
        budget = BudgetEntity(year=2025, limit=500.0, category_id=category.id)
        session.add(budget)
        session.flush()

        result = repr(budget)
        assert "Budget" in result
        assert "2025" in result
        assert "500.0" in result


def test_budget_entity_year_is_required(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _make_category(session)
        budget = BudgetEntity(limit=100.0, category_id=category.id)
        session.add(budget)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_budget_entity_limit_is_required(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _make_category(session)
        budget = BudgetEntity(year=2025, category_id=category.id)
        session.add(budget)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_budget_entity_category_id_is_required(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        budget = BudgetEntity(year=2025, limit=100.0)
        session.add(budget)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_budget_entity_unique_category_year(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _make_category(session)
        budget1 = BudgetEntity(year=2025, limit=300.0, category_id=category.id)
        budget2 = BudgetEntity(year=2025, limit=400.0, category_id=category.id)
        session.add(budget1)
        session.flush()
        session.add(budget2)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_budget_entity_different_years_allowed(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        category = _make_category(session)
        budget1 = BudgetEntity(year=2024, limit=300.0, category_id=category.id)
        budget2 = BudgetEntity(year=2025, limit=400.0, category_id=category.id)
        session.add(budget1)
        session.add(budget2)
        session.flush()

        assert budget1.id is not None
        assert budget2.id is not None


def test_budget_entity_different_categories_same_year_allowed(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        cat1 = _make_category(session, "Food")
        cat2 = _make_category(session, "Transport")
        budget1 = BudgetEntity(year=2025, limit=300.0, category_id=cat1.id)
        budget2 = BudgetEntity(year=2025, limit=150.0, category_id=cat2.id)
        session.add(budget1)
        session.add(budget2)
        session.flush()

        assert budget1.id is not None
        assert budget2.id is not None
