from flask import jsonify

from ..base import api, get_request_data, successful_response, BadRequest
from flask_login import login_required, login_user, current_user, logout_user

from App.Database import db
from App.Database.Models.user import User


@api.route('/login1', methods=['POST'])
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
        raise BadRequest('UserNotFound', 'user not found')

    if not user.check_password(password):
        raise BadRequest('WrongPassword', 'incorrect password')

    login_user(user, remember=False)

    return successful_response()


@api.route('/logout', methods=['GET'])
@login_required
def handle_logout():
    """
    This route authenticate the user.
    Method: GET
    Required: None
    """
    logout_user()
    return successful_response()


@api.route('/create_account', methods=['POST'])
def handle_create_account():
    """
    This route create a new user account.
    Method: POST
    Required:
        first_name: string
        last_name: string
        email: string
        password: string
    """
    data = get_request_data()

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

    try:
        new_user = User(email, password, first_name, last_name)
    except ValueError as e:
        raise BadRequest(str(e))

    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=False)

    return successful_response()


@api.route('/is_authenticated')
def handle_is_authenticated():
    """
    Method: GET
    :return: if user is authenticated or not
    """
    return {
        'authenticated': current_user.is_authenticated
    }


@api.route('/user_profile', methods=['GET'])
@login_required
def handle_user_profile():
    """
    This route return account basic info
    Methods: GET
    """
    return jsonify(
        {
            'id': current_user.id,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'email': current_user.email,
        }
    )


@api.route('/update_user_profile', methods=['POST'])
@login_required
def handle_user_profile_update():
    """
    This route update user profile
    Methods: POST
    Required:
        first_name: string
        last_name: string
    """
    data = get_request_data()
    try:
        current_user.first_name = data['first_name']
        current_user.last_name = data['last_name']
        db.session.commit()
        return successful_response('Save complete')
    except ValueError as e:
        raise BadRequest(str(e))


@api.route('/update_password', methods=['POST'])
@login_required
def handle_update_password():
    """
    This route update user password
    Methods: POST
    Required: current_password: str, new_password: str
    """
    data = get_request_data()
    current_password = data['current_password']
    new_password = data['new_password']

    if not current_user.check_password(current_password):
        raise BadRequest('WrongPassword', 'wrong password')

    try:
        current_user.password = new_password
        db.session.commit()
        return successful_response()
    except ValueError:
        pass

    raise BadRequest('ValueError', 'Unknown error occurred')

