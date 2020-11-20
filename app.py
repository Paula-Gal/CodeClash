from flask import Flask

from App.Blueprints.Landing import landing
from App.Blueprints.Dashboard import dashboard
from App.Blueprints.Dashboard import learningenv
from App.LoginManager import login_manager


app = Flask(__name__)

login_manager.init_app(app)

app.register_blueprint(landing)
app.register_blueprint(dashboard)
app.register_blueprint(learningenv)


app.run(debug=True)
