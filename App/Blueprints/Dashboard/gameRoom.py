from flask import render_template, url_for

from .base import gameRoom


@gameRoom.route('/room')
def handle_index():
    return render_template('gameRoom.html', title = 'Game Room')
    