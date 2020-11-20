from flask import render_template, url_for

from .base import dashboard


@dashboard.route('/dashboard')
def handle_index():
    return render_template('dashboard.html', title = 'Dashboard')

