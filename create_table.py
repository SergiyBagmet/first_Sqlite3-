from sqlite3 import Error, Connection

from connect import create_connection, database


def create_table(conn: Connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)    
        
if __name__ == '__main__':
    pass
    # with create_connection(database) as conn:
    #     if conn is not None:
    #         [create_table(conn, sql_create_table) for sql_create_table in sql_table_tasks]
    #     else:
    #         print("Error! cannot create the database connection.")        