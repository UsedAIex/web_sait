import sqlite3

# Основа добавления пользователей
def add(self):
    db_helper = DbHelper()
    con = sqlite3.connect('BASDT.db')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM BAS WHERE Пароль=?""", (password,)).fetchall()

    if result:
        pass

    elif len(name) == 0 or len(password) == 0:
        pass

    elif len(password) < 8 or password.upper() == password or password.lower() == password:
        pass

    else:
        result = db_helper.request("""INSERT INTO BAS('ИМЯ', 'Пароль') VALUES (?, ?)""",
                                   (name, password))
