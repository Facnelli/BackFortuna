from flask import Blueprint, request, jsonify
from functools import wraps

#Import adapters
from src.main.adapters.request_adapter import request_adapter

#import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

#import error handler
from src.errors.error_handler import handle_errors

user_routes_bp = Blueprint('user_routes', __name__)

def handle_route_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            http_response = func(*args, **kwargs)
        except Exception as e:
            http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code
    return wrapper

@user_routes_bp.route('/user/find', methods=['GET'])
@handle_route_errors
def find_user():
    return request_adapter(request, user_finder_composer())

@user_routes_bp.route('/user', methods=['POST'])
@handle_route_errors
def register_user():
    return request_adapter(request, user_register_composer())