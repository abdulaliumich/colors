from app import db

class Color(db.Model):
    color_name = db.Column(db.String(30), primary_key = True)
    
    def __init__(self, color_name):
        self.color_name = color_name
    
    def __repr__(self):
        return '<Color %r>' % self.color_name
