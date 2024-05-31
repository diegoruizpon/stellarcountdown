from app import app, db
from app.models import Event
from datetime import datetime

with app.app_context():
    db.create_all()

    event1 = Event(event_type='Lunar Eclipse', celestial_body='Moon', date=datetime(2024, 7, 27, 19, 0, 0))
    event2 = Event(event_type='Solar Eclipse', celestial_body='Sun', date=datetime(2024, 10, 14, 16, 0, 0))
    event3 = Event(event_type='Meteor Shower', celestial_body='Geminids', date=datetime(2024, 12, 13, 22, 0, 0))

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.commit()