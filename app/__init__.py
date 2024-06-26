from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config.from_pyfile('config.py', silent=True)  # Make sure the second argument is silent=True
db = SQLAlchemy(app)

from app import routes, models
