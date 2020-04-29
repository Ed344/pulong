from flask import render_template # serve page
from app import app

@app.route('/')
@app.route('/base')
def index():
    #return "Hello World"
    return render_template('base.html', title='base')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')
