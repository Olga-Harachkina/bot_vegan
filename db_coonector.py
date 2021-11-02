import sqlite3

def create_tables_new():
    cursor, con = get_connection()
    cursor.execute("""CREATE TABLE IF NOT EXISTS phone(
        name TEXT,
        number TEXT
        )""")
    con.commit()

def get_connection(db_name='test_database'):
    con = sqlite3.connect(db_name)
    return con.cursor(), con

def add_phone(name, phone):
    cursor, con = get_connection()
    cursor.execute("""INSERT INTO phone(name, number) VALUES(?, ?)""", [name, phone])
    con.commit()

def all_numbers():
    cursor, con = get_connection()
    result = cursor.execute("SELECT * FROM phone").fetchall()
    con.commit()
    return result
