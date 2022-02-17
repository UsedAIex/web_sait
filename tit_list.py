from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgmwebgip756b]PRQE*FPBGF*9wgovuY$%^*%i&*o()87RP5DOHpgw59tu3rgergfok&jy54whigbtrusgry3urfbhi'

@app.route('/')
def start():
    param = {}
    param['title'] = '1234'
    return render_template('title_list.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
