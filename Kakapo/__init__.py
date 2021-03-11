from flask import Flask

app = Flask(__name__)

import Kakapo.views.ui_views

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Device(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    ip_address = db.Column(db.Text)
    vendor = db.Column(db.Text)
    os = db.Column(db.Text)
    hostname = db.Column(db.Text)

db.create_all()

from Kakapo.controller.util import import_devices

for device in import_devices():
    device_obj = Device(**device)
    db.session.add(device_obj)

db.session.commit()