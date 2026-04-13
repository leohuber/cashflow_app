import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker  # noqa: TC002

from cashflow.data.db.entities import TransactionEntity


def test_transaction_entity_repr(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=99.99, account="Checking")
        session.add(transaction)
        session.flush()

        result = repr(transaction)
        assert "Transaction" in result
        assert "99.99" in result
        assert "Checking" in result


def test_transaction_entity_account_is_required(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=50.0)
        session.add(transaction)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_transaction_entity_amount_is_required(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(account="Savings")
        session.add(transaction)
        with pytest.raises((IntegrityError, Exception)):
            session.flush()


def test_transaction_entity_description_is_optional(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=10.0, account="Cash")
        session.add(transaction)
        session.flush()

        assert transaction.description is None


def test_transaction_entity_category_is_optional(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=10.0, account="Cash")
        session.add(transaction)
        session.flush()

        assert transaction.category is None
        assert transaction.category_id is None
