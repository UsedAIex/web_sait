from flask import Flask, render_template, redirect, request
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgmwebgip756b]PRQE*o)FPBGF*9wgovuY($%^*%i&*87RP5DOHpgw59tu3rgergfok&jy54whigbtrusgry3urfbhi'




class LoginForm(FlaskForm):
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form.html', title='Авторизация', form=form)



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
    app.run(port=8080, host='127.0.0.1')
