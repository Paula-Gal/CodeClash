from flask import Response, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException

from App.Database import db
from App.Database.Models.problem import Problem
from App.Database.Models.problem_test import ProblemTest


basic_auth = BasicAuth()


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class SecureModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


admin = Admin(name='CodeClash', template_mode='bootstrap3')


class ProblemModelView(SecureModelView):
    pass


class ProblemTestModelView(SecureModelView):
    pass


admin.add_view(ProblemModelView(Problem, db.session))
admin.add_view(ProblemTestModelView(ProblemTest, db.session))
