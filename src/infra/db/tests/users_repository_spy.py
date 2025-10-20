from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, user_name: str, email: str, password: str) -> None:
        self.insert_user_attributes["user_name"] = user_name
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

    def select_user(self, user_name: str) -> List[Users]:
        self.select_user_attributes["user_name"] = user_name
        return [
            Users(100, user_name, "email@gmail.com", "11122"),
            Users(101, user_name, "email2@gmail.com", "22222")
        ]


