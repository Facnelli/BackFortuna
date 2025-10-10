import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBconnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBconnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_user_name = 'name'
    mocked_email = 'name@gmail.com'
    mocked_senha = 'senha'
    
    users_repository = UsersRepository()
    users_repository.insert_user(mocked_user_name, mocked_email, mocked_senha)
    
    sql = '''
        SELECT * FROM users
        WHERE user_name = '{}'
        AND email = '{}'
        AND senha = '{}'
        '''.format(mocked_user_name, mocked_email, mocked_senha)
        
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    assert registry.user_name == mocked_user_name
    assert registry.email == mocked_email
    assert registry.senha == mocked_senha
    
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
                            '''))
    connection.commit()
    
@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    mocked_user_name = 'name2'
    mocked_email = 'name2@gmail.com'
    mocked_senha = 'senha2'
    
    sql = '''
        INSERT INTO users (user_name, email, senha) VALUES ('{}','{}','{}')
    '''.format(mocked_user_name, mocked_email, mocked_senha)
    
    connection.execute(text(sql))
    connection.commit()
    
    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_user_name)
    
    assert response[0].user_name == mocked_user_name
    assert response[0].email == mocked_email
    assert response[0].senha == mocked_senha
    
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
                            '''))
    connection.commit()