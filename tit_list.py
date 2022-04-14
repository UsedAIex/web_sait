# from flask import Flask, render_template, redirect
# from flask_wtf import FlaskForm
# import sqlite3
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

from flask import Flask, render_template, redirect

from data import db_session
from data.users import User
from form.user import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgmwebgip756b]PRQE*o)FPBGF*9wgovuY($%^*%i&*87RP5DOHpgw59tu3rgergfok&jy54whigbtrusgry3urfbhi'


def help_bd():
    db_session.global_init("bd/users.sqlite")


@app.route('/')
def start():
    form = RegisterForm()

    if form.validate_on_submit():
        print(RegisterForm.name)
        return redirect('/login')
    return render_template('title_list.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        us = User(
            name=form.name.data
        )
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")

        us.set_password(form.password.data)
        print(us.hashed_password)
        print(form.name)
        db_sess.add(us)
        db_sess.commit()
        return redirect('/')
    return render_template('registration2.html', title='Регистрация', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = RegisterForm()
    us = User()
    if form.validate_on_submit():
        us.set_password(form.password.data)
        print(us.hashed_password)
        print(form.name)
        return redirect('/')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def ew():
    print('sjvsbjhbh')


if __name__ == '__main__':
    help_bd()
    app.run(port=8080, host='127.0.0.1')
