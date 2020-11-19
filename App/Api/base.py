from flask import Blueprint, request, json, jsonify


api = Blueprint(
    'api',
    __name__,
    url_prefix='api'
)


class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, error, message='', payload=None):
        self.error = error
        self.message = message
        self.payload = payload


@api.errorhandler(BadRequest)
def handle_bad_request(error):
    """Catch BadRequest exception globally, serialize into JSON, and respond with 400."""
    payload = dict(error.payload or ())
    payload['error'] = error.error
    payload['status'] = 400
    payload['message'] = error.message
    return jsonify(payload), 400


def successful_response(message=''):
    return jsonify(
        {
            'status': 200,
            'message': message
        }
    ), 200


def get_request_data() -> dict:
    """
    :return: Request data as dict, must be called in a route context.
    """
    return json.loads(request.data)
