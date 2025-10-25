from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpNotFoundError, HttpBadRequestError

class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, user_name: str) -> Dict:
        self.__validate_name(user_name)
        users = self.__search_user(user_name)
        response = self.__format_response(users)

        return response

    @staticmethod
    def __validate_name(user_name: str) -> None:
        if not all(c.isalpha() or c.isspace() for c in user_name):
            raise HttpBadRequestError("Invalid user name")

        if len(user_name) > 50:
            raise HttpBadRequestError("User name is too long")

    def __search_user(self, user_name: str) -> List[Users]:
        users = self.__users_repository.select_user(user_name)
        if not users: raise HttpNotFoundError("User not found")

        return users

    @staticmethod
    def __format_response(users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({"user_name": user.user_name, "email": user.email})

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        return response
