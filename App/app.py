from flask import Flask

from App.Blueprints.Landing import landing
from App.LoginManager import login_manager


app = Flask(__name__)

login_manager.init_app(app)

app.register_blueprint(landing)


app.run(debug=True)
