from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, user_name: str, email: str, senha: str) -> None: pass

    @abstractmethod
    def select_user(self, user_name: str) -> List[Users]: pass



