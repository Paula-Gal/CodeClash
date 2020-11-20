from flask import Blueprint

dashboard = Blueprint(
    'dashboard',
    __name__,
    template_folder='templates'
)

learningenv = Blueprint(
    'learningenv',
    __name__,
    template_folder='templates'
)

gameRoom = Blueprint(
    'gameRoom',
    __name__,
    template_folder='templates'
)
waiting = Blueprint(
    'waiting',
    __name__,
    template_folder = 'templates'
)