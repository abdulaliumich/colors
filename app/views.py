from app import app, models, db, lm
from flask import render_template, request, redirect, url_for, session, g
from forms import NewUserForm
from models import User, Color
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        db.session.add(g.user)
        db.session.commit()
    else:
        print "not logged in"

@app.route('/')
@app.route('/index')
def index():
    print "This is the best website ever!"
    return render_template('index.html', title='Home')

@app.route('/colors')
def colors():
    colors = models.Color.query.all()
    return render_template('colors.html', title='Colors', colors=colors)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = NewUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        color = Color.query.filter_by(color_name = 'blue').first()
        print form.username.data
        db.session.add(user)
        user.add_color(color)
        db.session.commit()
        login_user(user)
        g.user = current_user
        return redirect(url_for('index'))
    return render_template('create_account.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(username):
    return User.query.get(username)
    
