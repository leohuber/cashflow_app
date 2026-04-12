from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from sqlalchemy.orm.relationships import _RelationshipDeclared

Base = declarative_base()


class CategoryEntity(Base):
    """Model representing a transaction category."""

    __tablename__ = "categories"

    id: Column[int] = Column(Integer, primary_key=True)
    name: Column[str] = Column(String, nullable=False, unique=True)
    description: Column[str] = Column(String, nullable=True)

    # Relationship with transactions
    transactions: _RelationshipDeclared[Any] = relationship("Transaction", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(name='{self.name}')>"


class TransactionEntity(Base):
    __tablename__ = "transactions"

    id: Column[int] = Column(Integer, primary_key=True)
    date: Column[datetime] = Column(DateTime, nullable=False, default=datetime.now)
    amount: Column[float] = Column(Float, nullable=False)
    description: Column[str] = Column(String, nullable=True)

    # Foreign key relationship with Category
    category_id: Column[int] = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category: _RelationshipDeclared[Any] = relationship("Category", back_populates="transactions")

    def __repr__(self) -> str:
        return f"<Transaction(date='{self.date}', amount={self.amount})>"
