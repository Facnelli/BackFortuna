from typing import Dict

class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, user_name: str) -> Dict:
        self.find_attributes['user_name'] = user_name

        return {
                "type": "Users",
                "count": 1,
                "attributes": [
                    {"user_name": user_name, "email": "user.email"}
                ]
        }