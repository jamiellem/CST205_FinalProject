from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/findPet')
def petSearch():
    return render_template('findPet.html')

@app.route('/signUp')
def CreateAcc():
    return render_template('CreateAcc.html')

@app.route('/login')
def Login():
    return render_template('Login.html')