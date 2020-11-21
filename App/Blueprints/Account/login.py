from flask import render_template, url_for

from .base import login


@login.route('/login', methods=['GET'])
def handle_login():
    return render_template('login.html', title = 'Login')
