from sqlalchemy.sql import func

from src import db


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False)
  active = db.Column(db.Boolean(), nullable=False)
  created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

  def __init__(self, username, email):
    self.username = username
    self.email = email
    self.active = True

