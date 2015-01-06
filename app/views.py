from app import app, models, db, lm
from flask import render_template, request, redirect, url_for, session, g, flash
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
    colors = Color.query.all()
    if g.user.is_authenticated():
        return render_template('colors.html', title='Colors', colors=colors, user_color=g.user.get_color(),
                                user_color_font=g.user.get_color_font())
    return render_template('colors.html', title='Colors', colors=colors, user_color=0)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = NewUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        color = Color.query.filter_by(color_name = form.color.data).first()
        print form.username.data
        db.session.add(user)
        user.add_color(color)
        db.session.commit()
        login_user(user)
        g.user = current_user
        user_color = user.get_color()
        flash ("Welcome to the " + user_color + " team, " + g.user.username + "!", 'color_flash')
        return redirect(url_for(user_color))
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
        user_color = user.get_color()
        next = request.args.get('next')
        
        if next: #being redirected to a color page the user was initially trying to access
            next = next.replace('/',"") #remove the '/' from the URL argument so the url_for function works
            if next != user_color: #the color page that the user is going to is not the user's color
                return redirect(url_for(next))
        flash ("Welcome back to the " + user_color + " team, " + g.user.username + "!", 'color_flash')
        return redirect(url_for(user_color))
    return render_template('login.html', form=form)

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(username):
    return User.query.get(username)

def handle_color_request(user_color, page_color, username):
    if user_color == page_color:
        color_page = "colors/" + user_color + ".html"
        return render_template(color_page, font=Color.query.filter_by(color_name = user_color).first().color_font)
    #wrong permissions
    flash ("Nice try, " + username + ", but you are on the " + user_color + " team!", 'color_flash')
    return redirect(url_for(user_color)) #send the user to his page with the flashed message



@app.route('/blue')
@login_required
def blue():
    return handle_color_request(g.user.get_color(), "blue", g.user.username)

@app.route('/red')
@login_required
def red():
    return handle_color_request(g.user.get_color(), "red", g.user.username)
 

@app.route('/green')
@login_required
def green():
    return handle_color_request(g.user.get_color(), "green", g.user.username)

@app.route('/yellow')
@login_required
def yellow():
    return handle_color_request(g.user.get_color(), "yellow", g.user.username)

@app.route('/orange')
@login_required
def orange():
    return handle_color_request(g.user.get_color(), "orange", g.user.username)

@app.route('/purple')
@login_required
def purple():
    return handle_color_request(g.user.get_color(), "purple", g.user.username)

    
