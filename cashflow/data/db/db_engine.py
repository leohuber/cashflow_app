from contextlib import contextmanager
from typing import TYPE_CHECKING

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from collections.abc import Generator

    from sqlalchemy.orm.session import Session


# Create the SQLAlchemy engine
class CashFlowDBEngine:
    def __init__(self, db_file: str) -> None:
        self.__db_url: str = f"sqlite:///{db_file}"
        self.__engine: Engine = create_engine(self.__db_url, connect_args={"check_same_thread": False})
        self.__sessionmaker: sessionmaker[Session] = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)

    @property
    def sqlalchemy_engine(self) -> Engine:
        return self.__engine

    @property
    def sessionmaker(self) -> sessionmaker[Session]:
        return self.__sessionmaker

    @property
    def engine(self) -> Engine:
        return self.__engine

    @contextmanager
    def get_session(self) -> Generator[Session]:
        """Get a database session as a context manager."""
        session = self.__sessionmaker()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
