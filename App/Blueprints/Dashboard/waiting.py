from flask import render_template, url_for
from flask_login import login_required

from .base import dashboard


@dashboard.route('/waiting-room')
@login_required
def handle_waiting():
    return render_template('waiting.html', title='Waiting room')
