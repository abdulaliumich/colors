from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

UserColors = db.Table ('UserColors',
             db.Column('username', db.String(50), db.ForeignKey('user.username')),
             db.Column('color_name', db.String(30), db.ForeignKey('color.color_name'))
)

class Color(db.Model):
    color_name = db.Column(db.String(30), primary_key = True)
    
    def __init__(self, color_name):
        self.color_name = color_name
    
    def __repr__(self):
        return '<Color %r>' % self.color_name

class User(db.Model):
    username = db.Column(db.String(50), primary_key = True)
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    colors = relationship('Color', secondary=UserColors,
                           backref=db.backref('UserColors', lazy='dynamic'),
                           lazy='dynamic')    

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.username)  # python 2
        except NameError:
            return str(self.username)  # python 3

    def add_color(self, color):
        if not self.has_color(color):
            self.colors.append(color)
            return self

    def has_color(self, color):
        if self.colors.filter(Color.color_name == color.color_name).count() > 0:
            return True
        return False

    def get_color(self):
        return self.colors[0].color_name
    
    def __repr__(self):
        return '<User %r>' % self.username
