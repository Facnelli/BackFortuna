from typing import Dict
from passlib.context import CryptContext
from email_validator import validate_email, EmailNotValidError
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError

# Contexto de hash(argon2)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def register(self, user_name: str, email: str, password: str) -> Dict:
        self.__validate_name(user_name)
        email_normalized = self.__validate_email(email)

        password_hash = self.__hash_password(password)

        self.__registry_user_data(user_name, email_normalized, password_hash)
        response = self.__format_response(user_name, email_normalized)
        return response

    @classmethod
    def __validate_name(cls, user_name: str) -> None:
        if not all(c.isalpha() or c.isspace() for c in user_name):
            raise HttpBadRequestError("Invalid user name")

        if len(user_name) > 25:
            raise HttpBadRequestError("User name is too long")

    @staticmethod
    def __validate_email(email: str) -> str:
        try:
            valid = validate_email(email)
            return valid.normalized
        except EmailNotValidError as e:
            raise HttpBadRequestError(f"Invalid email: {str(e)}")

    @staticmethod
    def __hash_password(password: str) -> str:
        if not password:
            raise HttpBadRequestError("Password cannot be empty")
        return pwd_context.hash(password)

    def __registry_user_data(self, user_name: str, email: str, password_hash: str) -> None:
        self.__user_repository.insert_user(user_name, email, password_hash)

    @classmethod
    def __format_response(cls, user_name: str, email: str) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "name": user_name,
                "email": email,
            }
        }

        return response