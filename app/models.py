from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(100), nullable=False)
    celestial_body = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
