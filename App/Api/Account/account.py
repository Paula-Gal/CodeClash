from ..base import api, get_request_data
from flask_login import login_required, login_user, current_user

from ...Database.Models.user import User


@api.route('/login', methods=['POST'])
def handle_login():
    """
    This route authenticate the user.
    Method: POST
    Required:
        email: string
        password: string
    Optional:
        remember_me: True|False, default False
    """
    data = get_request_data()
    email = str(data['email']).lower()
    password = str(data['password'])
    user = User.query.filter_by(_email=email).first()

    if not user:
        return 'False'
        # raise BadRequest('UserNotFound', 'user not found')

    if not user.check_password(password):
        return 'False'
        # raise BadRequest('WrongPassword', 'incorrect password')

    login_user(user, remember=True)

    return 'True'


@api.route('/logout', methods=['GET'])
@login_required
def handle_logout():
    """
    This route authenticate the user.
    Method: GET
    Required: None
    """
    login_user(current_user)
    return 'True'


@api.route('/create_account', methods=['POST'])
def handle_create_account():
    return 'create account api'
