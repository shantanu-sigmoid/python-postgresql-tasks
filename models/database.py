from psycopg2 import pool
import logging
from sqlalchemy import create_engine


class Database:

    __connection_pool = None

    @staticmethod
    def initialise(**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)
        logging.debug("Database Initialized")

    @staticmethod
    def get_connection():
        logging.info("Database Connected")
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()

class CursorFromConnectionPool:
    def __init__(self):
        self.conn = None
        self.cursor = None
        logging.info("Cursor Initialized from Database Connection")

    def __enter__(self):
        self.conn = Database.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:  # This is equivalent to `if exception_value is not None`
            self.conn.rollback()
            logging.warning("Rollback due to exception, ", exception_value)
        else:
            self.cursor.close()
            logging.info("Database Connection Closed")
            self.conn.commit()
        Database.return_connection(self.conn)

class Engine:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None
    def make_engine(self):
        try:
            self.engine = create_engine(self.connection_string)
            return self.engine
        except:
            logging.error("Creating engine failed. Connetion string not valid.")