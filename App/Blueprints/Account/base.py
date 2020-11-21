from flask import Blueprint

login = Blueprint(
    'account',
    __name__,
    template_folder='templates'
    # static_folder='App/static',
)
