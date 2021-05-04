from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.Boolean, default=False)