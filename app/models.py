from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

UserColors = db.Table ('UserColors',
             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
             db.Column('color_name', db.String(30), db.ForeignKey('color.color_name'))
)

class Color(db.Model):
    color_name = db.Column(db.String(30), primary_key = True)
    
    def __init__(self, color_name):
        self.color_name = color_name
    
    def __repr__(self):
        return '<Color %r>' % self.color_name

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique = True)
    username = db.Column(db.String(40), unique = True)
    colors = relationship("Color", secondary=UserColors, backref="user")    

    def __init__(self, username, email):
        self.username = username
        self.email = email

        def is_authenticated(self):
            return true
        
        def is_active(self):
            return True

        def is_anonymous(self):
            return False

        def get_id(self):
            try:
                return unicode(self.id)  # python 2
            except NameError:
                return str(self.id)  # python 3
    
    def __repr__(self):
        return '<User %r>' % self.username
