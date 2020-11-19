from flask import request, redirect, url_for
from flask_login import LoginManager

from App.Database.Models.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorised():
    return 'PLease login'
    # return redirect(url_for('', next=request.url))
