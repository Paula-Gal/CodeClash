import datetime
import random
from App.Websockets import websockets, ws_login_required, get_user_session_id
from ..base import get_request_data, api
from flask_login import current_user
from App.Database import Match, ProblemTest, db, User


def run_test(test: ProblemTest, code):
    pass


def test_code(code):
    return random.randint(0, 100) < 10

"""
@websockets.on('find_match')
@ws_login_required
def _handle_find_match(message):
    pass


@websockets.on('submit_code')
@ws_login_required
def _handle_submit_code(message):
    match = Match.query.filter_by(_red_user_id=current_user.id).fisrt()

    match = Match.query.filter_by(_blue_user_id=current_user.id).fisrt()

    test_code(message)"""

waiting_for_match = []


@websockets.on('find_game')
@ws_login_required
def _handle_find_game():
    global waiting_for_match

    if current_user.id not in waiting_for_match:
        waiting_for_match.append(current_user.id)

    print(current_user.email)

    if len(waiting_for_match) == 2:
        match = Match(waiting_for_match.pop(), waiting_for_match.pop(), True, datetime.timedelta(minutes=5))
        db.session.add(match)
        match.begin()
        db.session.commit()

        red_user = User.query.filter_by(id=match.red_user_id).first()
        blue_user = User.query.filter_by(id=match.blue_user_id).first()

        websockets.emit('start_game', {}, room=get_user_session_id(red_user))
        websockets.emit('start_game', {}, room=get_user_session_id(blue_user))


@websockets.on('cancel_game')
@ws_login_required
def _handle_cancel_game():
    global waiting_for_match

    if current_user.id in waiting_for_match:
        waiting_for_match.remove(current_user.id)
