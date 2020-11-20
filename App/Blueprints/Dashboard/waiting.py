from flask import render_template, url_for

from .base import waiting


@waiting.route('/waiting-room')
def handle_index():
    return render_template('waiting.html', title = 'Waiting room')
    