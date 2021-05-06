from application import db
from datetime import date

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(30), default='incompleted')
    date_created = db.Column(db.Date, nullable=False, default=date.today())