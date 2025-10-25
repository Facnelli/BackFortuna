class UserRegisterSpy:
    def __init__(self) -> None:
        self.user_name = None
        self.email = None
        self.password = None
        self.was_called = False

    def register(self, user_name: str, email: str, password: str) -> dict:
        self.was_called = True
        self.user_name = user_name
        self.email = email
        self.password = password
        return {
            "id": 1,
            "user_name": user_name,
            "email": email
        }
