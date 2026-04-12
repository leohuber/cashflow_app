from typing import TYPE_CHECKING

from cashflow.data.db.entities import CategoryEntity, TransactionEntity

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class CategoryDataAccess:
    """Data Access Object for Category entities."""

    @staticmethod
    def get_all_categories(session: Session) -> list[CategoryEntity]:
        """Retrieve all categories from the database."""
        return session.query(CategoryEntity).all()

    @staticmethod
    def get_category_by_id(session: Session, category_id: int) -> CategoryEntity | None:
        """Retrieve a category by its ID."""
        return session.query(CategoryEntity).filter(CategoryEntity.id == category_id).first()

    @staticmethod
    def save_category(session: Session, category: CategoryEntity) -> CategoryEntity:
        """Save a category to the database."""
        if category.id is None:
            # For new categories, use add() so the original object gets updated with the ID
            session.add(category)
            session.flush()  # This ensures the ID is populated
            return category
        # For existing categories, use merge()
        return session.merge(category)


class TransactionDataAccess:
    """Data Access Object for Transaction entities."""

    @staticmethod
    def get_all_transactions(session: Session) -> list[TransactionEntity]:
        """Retrieve all transactions from the database."""
        return session.query(TransactionEntity).all()

    @staticmethod
    def get_transaction_by_id(session: Session, transaction_id: int) -> TransactionEntity | None:
        """Retrieve a transaction by its ID."""
        return session.query(TransactionEntity).filter(TransactionEntity.id == transaction_id).first()

    @staticmethod
    def save_transaction(session: Session, transaction: TransactionEntity) -> TransactionEntity:
        """Save a transaction to the database."""
        if transaction.id is None:
            # For new transactions, use add() so the original object gets updated with the ID
            session.add(transaction)
            session.flush()  # This ensures the ID is populated
            return transaction
        # For existing transactions, use merge()
        return session.merge(transaction)

    @staticmethod
    def delete_transaction(session: Session, transaction_id: int) -> bool:
        """Delete a transaction by its ID."""
        transaction = TransactionDataAccess.get_transaction_by_id(session, transaction_id)
        if transaction:
            session.delete(transaction)
            return True
        return False
