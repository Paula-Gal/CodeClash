from flask import render_template, url_for
from flask_login import login_required

from .base import dashboard


@dashboard.route('/dashboard/learning-environment')
@login_required
def handle_leaning_environment():
    return render_template('learningenv.html', title='Code Clash learning env')

