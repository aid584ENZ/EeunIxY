# 代码生成时间: 2025-09-20 21:01:08
import logging
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose, MapCompose
from scrapy.utils.response import get_base_url
from scrapy.utils.python import to_bytes
import mysql.connector
from mysql.connector import Error

# Define your logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseMigrationTool:
    """
    A database migration tool using Scrapy framework.
    This tool is designed to migrate data from one database to another.
    """
    def __init__(self, source_db_config, target_db_config):
        """
        Initialize the database migration tool with source and target database configurations.
        :param source_db_config: A dictionary containing source database configuration.
        :param target_db_config: A dictionary containing target database configuration.
        """
        self.source_db_config = source_db_config
        self.target_db_config = target_db_config
        self.source_db_connection = None
        self.target_db_connection = None
        self.source_db_cursor = None
        self.target_db_cursor = None

    def connect_to_source_database(self):
        """
        Connect to the source database using the provided configuration.
        """
        try:
            self.source_db_connection = mysql.connector.connect(
                host=self.source_db_config['host'],
                user=self.source_db_config['user'],
                password=self.source_db_config['password'],
                database=self.source_db_config['database']
            )
            self.source_db_cursor = self.source_db_connection.cursor()
        except Error as e:
            logger.error(f"Failed to connect to source database: {e}")
            raise CloseSpider("Failed to connect to source database")

    def connect_to_target_database(self):
        """
        Connect to the target database using the provided configuration.
        """
        try:
            self.target_db_connection = mysql.connector.connect(
                host=self.target_db_config['host'],
                user=self.target_db_config['user'],
                password=self.target_db_config['password'],
                database=self.target_db_config['database']
            )
            self.target_db_cursor = self.target_db_connection.cursor()
        except Error as e:
            logger.error(f"Failed to connect to target database: {e}")
            raise CloseSpider("Failed to connect to target database")

    def migrate_data(self, table_name):
        """
        Migrate data from the source database to the target database for a given table.
        :param table_name: The name of the table to migrate data from.
        """
        try:
            # Fetch data from the source database
            self.source_db_cursor.execute(f"SELECT * FROM {table_name}")
            data = self.source_db_cursor.fetchall()

            # Insert data into the target database
            for row in data:
                insert_query = f"INSERT INTO {table_name} VALUES ({",".join(["%s"] * len(row))})"
                self.target_db_cursor.execute(insert_query, row)

            # Commit the changes to the target database
            self.target_db_connection.commit()
        except Error as e:
            logger.error(f"Failed to migrate data: {e}")
            raise CloseSpider("Failed to migrate data")

    def close_database_connections(self):
        "