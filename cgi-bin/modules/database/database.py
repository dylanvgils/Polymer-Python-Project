from modules.database import config
import sqlite3

def init_db(filename = "modules/database/idp.sql"):
    """ Executes a SQL file
    """

    with open(filename, 'r') as scriptfile:
        conn = sqlite3.connect(config.DB['file'])
        try:
            script = scriptfile.read()
            conn.executescript(script)
        except Exception as e:
            conn.rollback()
            raise
        finally:
            conn.close()

def query(sql, args = ()):
    """ Executes a SQL query and returns it's results.
    """

    result = []

    conn = sqlite3.connect(config.DB['file'])
    conn.row_factory = sqlite3.Row

    try:
        cur = conn.execute(sql, args)

        sqlStatement = (sql.split(' '))[0].lower()
        if sqlStatement in ['select', 'show']:
            result = cur.fetchall()
        elif sqlStatement in ['insert', 'update', 'delete']:
            result = cur.rowcount
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()

    return result

def row(sql, args = ()):
    """ Executes a SQL query and returns a single row as result
    """


    result = query(sql, args)
    if result:
        return result[0]

def single(sql, args = ()):
    """ Executes a SQL query and returns a single column as result
    """

    result = query(sql, args)
    if result:
        return result[0][0]
