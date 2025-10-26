from .user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator():
    request = MockRequest()
    request.json = {
        "user_name": "Nome de usu",
        "email": "a43sddas@gmail.com",
        "password": "Aa1",
    }

    user_register_validator(request)