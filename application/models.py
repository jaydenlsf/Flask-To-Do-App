from application import db
from datetime import datetime
import pytz


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False, unique=True)
    status = db.Column(db.String(15), default="incompleted")
    date_created = db.Column(db.Date, default=datetime.now(pytz.timezone("Europe/London")).date())
