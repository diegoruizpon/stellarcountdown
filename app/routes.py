from flask import render_template
from app import app
from app.models import Event

@app.route('/')
def index():
    
    events = Event.query.all()
    
    return render_template('index2.html')
    #return render_template('index.html', events=events)
