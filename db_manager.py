from contextlib import contextmanager
import sqlite3
from sqlite3 import Error, Cursor
from pathlib import Path
import typing as t


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
        if not value.exists() or not value.is_file():
            conn = sqlite3.connect(value)
            conn.close()     
        self._db_file = value
    
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

    def create(self, create_sql, param: t.Iterable[t.Any]=()):
        with self.db_manager.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(create_sql, param)
    
    def parse_select_cursor(self, cursor: Cursor):
        data = cursor.fetchall()
        columns = [tuple(description[0] for description in cursor.description)]
        columns.extend(data)
        return columns
    
    def execute_select_from_file(self, script_file, param: t.Iterable[t.Any]=()):
        with open(script_file, "r") as sql_file:
            select_query = sql_file.read()
        with self.db_manager.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(select_query, param)
            return self.parse_select_cursor(cursor)
    
    def execute_many_sql(self, sql, param: t.Iterable[t.Any]=()):
        with self.db_manager.create_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, param)
           
    def execute_sql_script(self, script_file):
        with self.db_manager.create_connection() as conn:
            cursor = conn.cursor()
            with open(script_file, "r") as sql_file:
                sql_script = sql_file.read()
            cursor.executescript(sql_script)
      
    
if __name__ == "__main__":
    pass
       