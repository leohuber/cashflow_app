from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class CategoryEntity(Base):
    """Model representing a transaction category."""

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None] = mapped_column(default=None)

    # Relationship with transactions
    transactions: Mapped[list[TransactionEntity]] = relationship("TransactionEntity", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(name='{self.name}')>"


class TransactionEntity(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column(default=datetime.now)
    amount: Mapped[float] = mapped_column()
    description: Mapped[str | None] = mapped_column(default=None)

    # Foreign key relationship with Category
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), default=None)
    category: Mapped[CategoryEntity | None] = relationship("CategoryEntity", back_populates="transactions")

    def __repr__(self) -> str:
        return f"<Transaction(date='{self.date}', amount={self.amount})>"
