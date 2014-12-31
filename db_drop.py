#!venv/bin/python
from app import db
from config import SQLALCHEMY_DATABASE_URI

print "dropping tables"

db.drop_all()
