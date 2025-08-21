# 代码生成时间: 2025-08-22 01:38:20
import logging
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from scrapy.utils.response import response_status_message
import sqlite3
import psycopg2


# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseMigrationTool(Spider):
    '''
    数据库迁移工具，用于将SQLite数据库迁移到PostgreSQL数据库。
    '''
    name = 'database_migration_tool'
    allowed_domains = ['']  # 注意：这里需要填写实际的域名
    start_urls = ['http://example.com/']  # 示例URL，需要替换为目标数据库的URL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 连接SQLite数据库
        self.sqlite_conn = sqlite3.connect('your_sqlite_database.db')
        self.sqlite_cursor = self.sqlite_conn.cursor()

        # 连接PostgreSQL数据库
        self.postgres_conn = psycopg2.connect(
            dbname='your_dbname',
            user='your_user',
            password='your_password',
            host='your_host',
            port='your_port'
        )
        self.postgres_cursor = self.postgres_conn.cursor()

    def parse(self, response):
        '''
        解析SQLite数据库中的表，并迁移到PostgreSQL数据库。
        '''
        # 检查响应状态
        if response.status != 200:
            logger.error(response_status_message(response))
            raise CloseSpider(response_status_message(response))

        # 从SQLite数据库中获取表结构
        self.sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.sqlite_cursor.fetchall()

        for table in tables:
            table_name = table[0]
            logger.info(f'开始迁移表：{table_name}')

            # 迁移表结构
            self._migrate_table_structure(table_name)

            # 迁移表数据
            self._migrate_table_data(table_name)

    def _migrate_table_structure(self, table_name):
        '''
        迁移表结构到PostgreSQL数据库。
        '''
        # 获取SQLite表结构
        self.sqlite_cursor.execute(f'PRAGMA table_info({table_name});')
        columns = self.sqlite_cursor.fetchall()

        # 创建PostgreSQL表结构
        column_definitions = [f'"{column[1]}" {self._get_postgres_type(column[2])}' for column in columns]
        create_table_query = f'CREATE TABLE "{table_name}" ({", ".join(column_definitions)});'

        try:
            self.postgres_cursor.execute(create_table_query)
            self.postgres_conn.commit()
            logger.info(f'表结构迁移成功：{table_name}')
        except psycopg2.Error as e:
            logger.error(f'迁移表结构失败：{e}')
            self.postgres_conn.rollback()

    def _migrate_table_data(self, table_name):
        '''
        迁移表数据到PostgreSQL数据库。
        '''
        # 获取SQLite表数据
        self.sqlite_cursor.execute(f'SELECT * FROM {table_name};')
        records = self.sqlite_cursor.fetchall()

        # 插入数据到PostgreSQL表
        for record in records:
            placeholders = ', '.join(['%s'] * len(record))
            columns = ', '.join([f'"{column[1]}"' for column in self.sqlite_cursor.description])
            insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders});'

            try:
                self.postgres_cursor.execute(insert_query, record)
                self.postgres_conn.commit()
            except psycopg2.Error as e:
                logger.error(f'迁移数据失败：{e}')
                self.postgres_conn.rollback()

    def _get_postgres_type(self, sqlite_type):
        '''
        根据SQLite数据类型获取对应的PostgreSQL数据类型。
        '''
        # 这里可以根据实际情况扩展更多的数据类型映射
        if sqlite_type == 'INTEGER':
            return 'SERIAL'
        elif sqlite_type == 'TEXT':
            return 'VARCHAR(255)'
        elif sqlite_type == 'REAL':
            return 'DOUBLE PRECISION'
        else:
            return 'TEXT'

    def closed(self, reason):
        '''
        关闭数据库连接。
        '''
        self.sqlite_conn.close()
        self.postgres_conn.close()
        logger.info('数据库连接已关闭')
