from flask import render_template, url_for

from .base import gameRoom


@gameRoom.route('/room/<code>')
def profile(code):
    return render_template('gameRoom.html', title = 'Game Room', code = code)
    