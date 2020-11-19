import flask_socketio
import functools
from flask_login import current_user


def ws_login_required(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            flask_socketio.disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped


websockets = flask_socketio.SocketIO(ping_timeout=30, async_mode='gevent')
