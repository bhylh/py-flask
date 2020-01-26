from flask import Flask, escape, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@app.route('/user/<username>')
def show_user_profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)