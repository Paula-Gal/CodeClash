from flask import render_template, url_for
from flask_login import login_required

from .base import dashboard


@dashboard.route('/room')
@login_required
def handle_room():
    return render_template('gameRoom.html', title='Game Room')
