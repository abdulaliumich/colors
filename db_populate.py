#!venv/bin/python
from app import db, models

print "populating tables"

blue = models.Color('blue', 'blue')
red = models.Color('red', 'red')
green = models.Color('green', 'green')
yellow = models.Color('yellow', 'gold')
orange = models.Color('orange', 'orange')
purple = models.Color('purple', 'purple')

db.session.add(blue)
db.session.add(red)
db.session.add(green)
db.session.add(yellow)
db.session.add(orange)
db.session.add(purple)

db.session.commit()

