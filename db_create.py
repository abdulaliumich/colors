#!venv/bin/python
from app import db
from config import SQLALCHEMY_DATABASE_URI

print "creating tables"

db.create_all()
