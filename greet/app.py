from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home!"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome Back!"