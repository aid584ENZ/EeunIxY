# 代码生成时间: 2025-08-10 10:59:07
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

"""
Database Pool Manager using Scrapy and SQLAlchemy.
This module manages a database connection pool for Scrapy projects."""

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabasePoolManager:
    def __init__(self, database_url, max_overflow=10, pool_size=5, pool_timeout=30):
        """
        Initializes the database pool manager.
        :param database_url: The URL of the database to connect to.
        :param max_overflow: The maximum number of overflow connections.
        :param pool_size: The size of the connection pool.
        :param pool_timeout: The timeout in seconds for waiting for a connection.
        """
        self.database_url = database_url
        self.max_overflow = max_overflow
        self.pool_size = pool_size
        self.pool_timeout = pool_timeout
        self.engine = None
        self.Session = None
        self._create_engine()
        self._create_session_maker()

    def _create_engine(self):
        """
        Creates a SQLAlchemy engine with connection pooling.
        """
        try:
            self.engine = create_engine(self.database_url,
                                       poolclass=QueuePool,
                                       pool_size=self.pool_size,
                                       max_overflow=self.max_overflow,
                                       pool_timeout=self.pool_timeout)
        except SQLAlchemyError as e:
            logger.error(f"Failed to create engine: {e}")
            raise

    def _create_session_maker(self):
        """
        Creates a session maker bound to the engine's connection pool.
        """
        try:
            Session = sessionmaker(bind=self.engine)
            self.Session = Session
        except SQLAlchemyError as e:
            logger.error(f"Failed to create session maker: {e}")
            raise

    def get_session(self):
        """
        Returns a new session from the pool.
        """
        try:
            session = self.Session()
            return session
        except SQLAlchemyError as e:
            logger.error(f"Failed to get session: {e}")
            raise

    def close_all(self):
        """
        Closes all sessions in the pool.
        """
        try:
            self.Session.close_all()
        except SQLAlchemyError as e:
            logger.error(f"Failed to close all sessions: {e}")
            raise

# Example usage
if __name__ == "__main__":
    database_url = "mysql+pymysql://user:password@localhost:3306/scrapy_db"
    db_manager = DatabasePoolManager(database_url)
    session = db_manager.get_session()
    # Perform database operations using the session
    db_manager.close_all()