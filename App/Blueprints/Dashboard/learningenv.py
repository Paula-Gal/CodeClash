from flask import render_template, url_for

from .base import learningenv


@learningenv.route('/dashboard/learning-environment')
def handle_index():
    return render_template('learningenv.html', title = 'Code Clash learning env')

