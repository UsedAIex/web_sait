from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField
class LoginForm(FlaskForm):
    submit = SubmitField('Войти')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgmwebgip756b]PRQE*o)FPBGF*9wgovuY($%^*%i&*87RP5DOHpgw59tu3rgergfok&jy54whigbtrusgry3urfbhi'

@app.route('/')
def start():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('title_list.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form.html', title='Авторизация', form=form)

@app.route('/success', methods=['GET', 'POST'])
def ew():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
