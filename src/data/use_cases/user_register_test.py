from passlib.context import CryptContext
from src.infra.db.tests.users_repository_spy import UsersRepositorySpy
from .user_register import UserRegister

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def test_register():
    user_name = "nominho"
    email = "1@gmail.com"
    password = "123123"

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(user_name, email, password)

    assert repo.insert_user_attributes["user_name"] == user_name
    assert repo.insert_user_attributes["email"] == email

    stored_hash = repo.insert_user_attributes["password"]
    assert pwd_context.verify(password, stored_hash)

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_name_error():
    user_name = "nominho132"
    email = "1@gmail.com"
    password = "123123"

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(user_name, email, password)
        assert False
    except Exception as e:
        assert str(e) == "Invalid user name"

def test_register_email_error():
    user_name = "nominho"
    email = "teste@.com"
    password = "123123"

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(user_name, email, password)
        assert False
    except Exception as e:
        assert "Invalid email" in str(e)