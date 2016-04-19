from flask import Flask, request, jsonify, render_template
from flask.ext.redis import FlaskRedis

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
