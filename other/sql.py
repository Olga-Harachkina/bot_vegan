import sqlite3 as sq
with sq.conect('hijack.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS eda (
    name TEXT,
    composition TEXT,
    price REAL,
    gram INTEGER
     )""")
    con.commit()



    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    sex TEXT,
    name TEXT,
    number INTEGER
     )""")
    con.commit()
    user_sex = input('sex: ')
    user_name = input('name: ')
    user_number = input('number: ')
    cur.execute(f"SELECT number FROM users WHERE number ='{user_number}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?,?,?)", (user_sex, user_name, user_number))
        con.commit()

        print('добавлен')
    else:
        print('have')

        for value in con.execute("SELECT * FROM users"):
            print(value)


