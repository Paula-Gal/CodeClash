from flask import render_template, url_for
from flask_login import login_required

from .base import dashboard


@dashboard.route('/dashboard')
@login_required
def handle_index():
    return render_template('dashboard.html', title = 'Dashboard')

