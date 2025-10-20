from abc import ABC, abstractmethod
from typing import Dict

class UserRegister(ABC):

    @abstractmethod
    def register(self, user_name: str, email: str, password: str) -> Dict: pass
