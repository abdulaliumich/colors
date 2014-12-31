#!venv/bin/python
from app import db, models

print "populating tables"

blue = models.Color('blue')
red = models.Color('red')
green = models.Color('green')
yellow = models.Color('yellow')
orange = models.Color('orange')
purple = models.Color('purple')

db.session.add(blue)
db.session.add(red)
db.session.add(green)
db.session.add(yellow)
db.session.add(orange)
db.session.add(purple)

db.session.commit()

