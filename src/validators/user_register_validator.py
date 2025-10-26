from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_register_validator(request: any):

    body_validator = Validator({
        "user_name": { 'type': 'string', 'required': True, "empty": False },
        "email": {'type': 'string', 'required': True, "empty": False},
        "password": {'type': 'string', 'required': True, "empty": False, 'regex': '^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).+$'},
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)