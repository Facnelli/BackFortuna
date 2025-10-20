from src.infra.db.repositories import users_repository
from src.infra.db.tests.users_repository_spy import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    user_name = "meunome"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(user_name)

    assert repo.select_user_attributes["user_name"] == user_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    user_name = "meuNome123"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(user_name)
        assert False
    except Exception as e:
        assert str(e) == "Invalid user name"

def test_find_error_in_long_name():
    user_name = "meuNomeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(user_name)
        assert False
    except Exception as e:
        assert str(e) == "User name is too long"

def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, user_name: str): return []

    user_name = "meuNome"
    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(user_name)
        assert False
    except Exception as e:
        assert str(e) == "User not found"