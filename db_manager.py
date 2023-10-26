from contextlib import contextmanager
import sqlite3
from sqlite3 import Error, Connection
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_file: str | Path):
        self._db_file = None
        self.db_file = db_file

    @property
    def db_file(self):
        return self._db_file

    @db_file.setter
    def db_file(self, value: str | Path):
        if isinstance(value, str): value = Path(value)
        if not value.is_file():
            self._create_database(value)
        self._db_file = value
    
    def _create_database(self, value=None):
        """ create a database, if not exists """
        conn = sqlite3.connect(self.db_file or value)
        conn.close()
    
    @contextmanager
    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = sqlite3.connect(self.db_file)
        try:
            yield conn
            conn.commit()
        except Error as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()

class CRUDManager:
    def __init__(self, database_manager: DatabaseManager):
        self.db_manager = database_manager

    def create_table(self, create_table_sql):
        with self.db_manager.create_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(create_table_sql)
            except Error as e:
                print(e)

    def create_tables(self, create_tables_sql):
        with self.db_manager.create_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.executemany(create_tables_sql)
            except Error as e:
                print(e)

    def execute_sql_script(self, script_file):
        with self.db_manager.create_connection() as conn:
            try:
                cursor = conn.cursor()
                with open(script_file, "r") as sql_file:
                    sql_script = sql_file.read()
                cursor.executescript(sql_script)
            except Error as e:
                print(e)
                
if __name__ == "__main__":
    pass
    # database = './university.db'
    # dbm = DatabaseManager(database)
    # crud = CRUDManager(dbm)
    # crud.execute_sql_script("./SQL/create_tabels.sql")         