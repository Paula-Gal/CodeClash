from flask import Flask

from App.Database import db
from App.Blueprints.Landing import landing
from App.LoginManager import login_manager
from App.Blueprints.Administrator import admin
from App.Websockets.base import websockets
from config import BasicConfig


app = Flask(__name__)

app.config.from_object(BasicConfig)

db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(landing)


admin.init_app(app)


with app.app_context():
    db.create_all()

websockets.init_app(app)

websockets.run(app, log_output=True, port=5000)
# app.run(debug=True)
