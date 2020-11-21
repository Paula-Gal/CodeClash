from flask import Flask

from App.Blueprints.Landing import landing
from App.Blueprints.Dashboard import dashboard
from App.Database import db
from App.LoginManager import login_manager
from App.Blueprints.Administrator import admin
from App.Blueprints.Account import login
from App.Tests.database import populate_database
from App.Websockets import websockets
from config import BasicConfig
from App.Api import api


app = Flask(__name__)

app.config.from_object(BasicConfig)

db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(landing)
app.register_blueprint(dashboard)
app.register_blueprint(login)
app.register_blueprint(api)

admin.init_app(app)


with app.app_context():
    db.create_all()
    populate_database()

websockets.init_app(app)

websockets.run(app, log_output=True, debug=True, port=5000, host='localhost')
