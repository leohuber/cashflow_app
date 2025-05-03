import datetime as dt
from datetime import datetime
from pathlib import Path

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship, sessionmaker

Base = declarative_base()


class Category(Base):
    """Model representing a transaction category."""

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    # Relationship with transactions
    transactions = relationship("Transaction", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(name='{self.name}')>"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    # Foreign key relationship with Category
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="transactions")

    def __repr__(self) -> str:
        return f"<Transaction(date='{self.date}', amount={self.amount})>"


class DatabaseManager:
    def __init__(self, db_path: Path | None = None) -> None:
        if db_path is None:
            msg: str = "db_path must be provided"
            raise ValueError(msg)

        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self) -> None:
        """Create all tables defined in the models."""
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        """Return a new database session."""
        return self.SessionLocal()

    def add_category(self, name: str, description: str | None = None) -> Category:
        """Add a new category to the database."""
        with self.get_session() as session:
            category = Category(name=name, description=description)
            session.add(category)
            session.commit()
            session.refresh(category)
            return category

    def add_transaction(
        self,
        amount: float,
        description: str | None = None,
        category_id: int | None = None,
        date: datetime | None = None,
    ) -> Transaction:
        """Add a new transaction to the database."""
        with self.get_session() as session:
            transaction = Transaction(amount=amount, description=description, category_id=category_id, date=date or datetime.now(tz=dt.UTC))
            session.add(transaction)
            session.commit()
            session.refresh(transaction)
            return transaction

    def get_all_categories(self) -> list[Category]:
        """Retrieve all categories from the database."""
        with self.get_session() as session:
            return list(session.execute(select(Category)).scalars().all())

    def get_all_transactions(self) -> list[Transaction]:
        """Retrieve all transactions from the database."""
        with self.get_session() as session:
            return list(session.execute(select(Transaction)).scalars().all())
