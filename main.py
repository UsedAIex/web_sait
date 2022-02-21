from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def help_bd(login, password):
    con = sqlite3.connect("C:/Users/Владимир/PycharmProjects/pythonProject1/venv/login.db")
    cur = con.cursor()
    cur.execute('INSERT INTO registr(id, password, login) VALUES(?, ?, ?)',
                (len(all) + 1, str(password), str(login)))
    all = cur.execute('SELECT * FROM registr').fetchall()
    print(all)
    con.commit()
    con.close()


@app.route('/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(login)
        help_bd(login, password)
    else:
        return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=False)