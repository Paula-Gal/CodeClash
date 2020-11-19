from flask import render_template, url_for

from .base import landing


@landing.route('/')
def handle_index():
    return render_template('index.html')


@landing.route('/test')
def handle_test():
    return 'ok'
