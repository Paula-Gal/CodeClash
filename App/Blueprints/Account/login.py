from flask import render_template, url_for

from .base import login


@login.route('/login')
def handle_index():
    return render_template('login.html', title = 'Login')
