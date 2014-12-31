from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    print "This is the best website ever!"
    return render_template('index.html', title='Home')

@app.route('/colors')
def colors():
    return render_template('colors.html', title='Colors')
