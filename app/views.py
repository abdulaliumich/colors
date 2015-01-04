from app import app, models, db, lm
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    print "This is the best website ever!"
    return render_template('index.html', title='Home')

@app.route('/colors')
def colors():
    colors = models.Color.query.all()
    return render_template('colors.html', title='Colors', colors=colors)

@app.route('/login')
def login():
    return render_template('login.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
