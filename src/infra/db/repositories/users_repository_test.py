from src.infra.db.settings.connection import DBconnectionHandler
from .users_repository import UsersRepository

def test_insert_user():
    mocked_user_name = 'name'
    mocked_email = 'name@gmail.com'
    mocked_senha = 'senha'
    
    users_repository = UsersRepository()
    users_repository.insert_user(mocked_user_name, mocked_email, mocked_senha)