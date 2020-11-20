from flask import request

from .base import websockets, ws_login_required


@websockets.on('connect')
@ws_login_required
def _handle_connect():
    print('<WS>: Client ' + str(request.sid) + ' connected')
    pass


@websockets.on('disconnect')
def _handle_disconnect():
    print('<WS>: Client ' + str(request.sid) + ' disconnected')
    pass


@websockets.on_error()  # Handles the default namespace
def _error_handler(e):
    pass


@websockets.on('message')
@ws_login_required
def _handle_message(message):
    print('<WS>: Received message: ' + message)
    pass


@websockets.on('find_match')
@ws_login_required
def _handle_find_match():
    pass
