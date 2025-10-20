from typing import List
from src.infra.db.settings.connection import DBconnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UsersRepository(UsersRepositoryInterface):
    
    @classmethod
    def insert_user(cls, user_name: str, email: str, password: str) -> None:
        with DBconnectionHandler() as database: 
            try:
                new_resistry = UsersEntity(
                    user_name = user_name,
                    email = email,
                    password = password,
                )
                database.session.add(new_resistry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    @classmethod
    def select_user(cls, user_name: str) -> List[Users]:
        with DBconnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.user_name == user_name)
                        .all()
                )
                return users
            
            except Exception as exception:
                database.session.rollback()
            raise exception
        

    