import random

from App.Websockets import websockets, ws_login_required
from ..base import get_request_data, api

from flask_login import current_user

from App.Database import Match, ProblemTest


def run_test(test: ProblemTest, code):
    pass


def test_code(code):
    return random.randint(0, 100) < 10


@websockets.on('find_match')
@ws_login_required
def _handle_find_match(message):
    pass


@websockets.on('submit_code')
@ws_login_required
def _handle_submit_code(message):
    match = Match.query.filter_by(_red_user_id=current_user.id).fisrt()

    match = Match.query.filter_by(_blue_user_id=current_user.id).fisrt()

    test_code(message)

