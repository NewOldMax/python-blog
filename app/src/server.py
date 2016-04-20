from flask import Flask, render_template, redirect, flash
from flask.ext.redis import FlaskRedis
from forms import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    user = { 'username': 'John' }
    posts = [
        { 
            'author': { 'username': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'username': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)