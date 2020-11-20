from flask import request
from flask_login import current_user
from flask_socketio import join_room, emit

from .base import websockets, ws_login_required


@websockets.on('connect')
#@ws_login_required
def _handle_connect():
    print('<WS>: Client ' + str(request.sid) + ' connected')
    #join_room(current_user.email)
    websockets.emit('msg', data = "salut")
    pass


@websockets.on('disconnect')
def _handle_disconnect():
    #print('<WS>: Client ' + str(request.sid) + ' disconnected')
    pass


@websockets.on_error()  # Handles the default namespace
def _error_handler(e):
    pass


@websockets.on('message')
@ws_login_required
def _handle_message(message):
    print('<WS>: Received message: ' + message)
    pass

