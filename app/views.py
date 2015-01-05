from app import app, models, db, lm
from flask import render_template, request, redirect, url_for, session, g
from forms import NewUserForm, LoginForm
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
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        password = form.password.data
        if user.password != form.password.data:
            return render_template('login.html', form=form, errorMessage="Username and password don't match!") 
            #doing username/password check here because i don't know how to do it in wtforms
        login_user(user)
        g.user = current_user
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(username):
    return User.query.get(username)
    
