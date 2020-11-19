from flask import Blueprint, request, json


api = Blueprint(
    'api',
    __name__,
    url_prefix='api'
)


def get_request_data() -> dict:
    """
    :return: Request data as dict, must be called in a route context.
    """
    return json.loads(request.data)
