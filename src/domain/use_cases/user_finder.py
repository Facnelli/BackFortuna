from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):

    @abstractmethod
    def find(self, user_name: str) -> Dict: pass
