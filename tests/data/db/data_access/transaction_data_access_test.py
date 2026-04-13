from datetime import UTC, datetime

from sqlalchemy.orm import sessionmaker  # noqa: TC002

from cashflow.data.db.data_access import TransactionDataAccess
from cashflow.data.db.entities import TransactionEntity


def test_get_all_transactions(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        t1 = TransactionEntity(amount=10.0, account="Checking")
        t2 = TransactionEntity(amount=20.0, account="Savings")
        t3 = TransactionEntity(amount=30.0, account="Cash")

        TransactionDataAccess.save_transaction(session, t1)
        TransactionDataAccess.save_transaction(session, t2)
        TransactionDataAccess.save_transaction(session, t3)
        session.commit()

        transactions = TransactionDataAccess.get_all_transactions(session)

        assert len(transactions) == 3
        assert any(t.id == t1.id for t in transactions)
        assert any(t.id == t2.id for t in transactions)
        assert any(t.id == t3.id for t in transactions)


def test_get_transaction_by_id(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=42.0, account="Checking")
        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        retrieved = TransactionDataAccess.get_transaction_by_id(session, transaction.id)

        assert retrieved is transaction


def test_get_transaction_by_id_not_found(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        result = TransactionDataAccess.get_transaction_by_id(session, 9999)
        assert result is None


def test_save_new_transaction_assigns_id(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=15.0, account="Savings")
        assert transaction.id is None

        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        assert transaction.id is not None


def test_save_existing_transaction_updates_record(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=100.0, account="Checking")
        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        transaction.account = "Savings"
        transaction.amount = 200.0
        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        retrieved = TransactionDataAccess.get_transaction_by_id(session, transaction.id)
        assert retrieved is not None
        assert retrieved.account == "Savings"
        assert retrieved.amount == 200.0


def test_save_transaction_with_account(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(
            amount=75.5,
            account="Business",
            date=datetime(2026, 1, 15, tzinfo=UTC),
        )
        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        retrieved = TransactionDataAccess.get_transaction_by_id(session, transaction.id)
        assert retrieved is not None
        assert retrieved.account == "Business"
        assert retrieved.amount == 75.5


def test_delete_transaction(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        transaction = TransactionEntity(amount=50.0, account="Cash")
        TransactionDataAccess.save_transaction(session, transaction)
        session.commit()

        saved_id = transaction.id
        result = TransactionDataAccess.delete_transaction(session, saved_id)
        session.commit()

        assert result is True
        assert TransactionDataAccess.get_transaction_by_id(session, saved_id) is None


def test_delete_transaction_not_found(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        result = TransactionDataAccess.delete_transaction(session, 9999)
        assert result is False
