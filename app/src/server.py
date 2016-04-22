import json
from flask import Flask, render_template, redirect, flash, url_for, session, request, g, jsonify
from flask.ext.redis import FlaskRedis
from forms import LoginForm, RegisterForm, PostForm

app = Flask(__name__)
app.config.update(
    REDIS_URL="redis://redis:6379/0"
)
redis_store = FlaskRedis(app)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'dkfj273hf784h1dj98q'

app.debug = True

@app.route('/')
def index():
    user = {}
    posts = redis_store.get('posts')
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('form.html', 
        title = 'Sign In',
        form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('form.html', 
        title = 'Sign Up',
        form = form)

@app.route('/post', methods = ['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        redis_store.set('posts', {'title':form.title.data,'text':form.text.data})
        return redirect(url_for('index'))
    return render_template('form.html', 
        title = 'Create Post',
        form = form)