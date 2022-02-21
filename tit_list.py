from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, request
import sqlite3
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    submit = SubmitField('Войти')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgmwebgip756b]PRQE*o)FPBGF*9wgovuY($%^*%i&*87RP5DOHpgw59tu3rgergfok&jy54whigbtrusgry3urfbhi'


def help_bd(login, password):
    con = sqlite3.connect("C:/Users/Владимир/PycharmProjects/pythonProject1/venv/login.db")
    cur = con.cursor()
    cur.execute('INSERT INTO registr(id, password, login) VALUES(?, ?, ?)',
                (len(all) + 1, str(password), str(login)))
    all = cur.execute('SELECT * FROM registr').fetchall()
    print(all)
    con.commit()
    con.close()

@app.route('/')
def start():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('title_list.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(login)
        help_bd(login, password)
    else:
        return render_template('registration.html')


@app.route('/success', methods=['GET', 'POST'])
def ew():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
