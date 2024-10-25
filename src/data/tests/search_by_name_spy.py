from typing import Dict

class SearchByNameSpy:
    def __init__(self):
        self.search_attribute = {}

    def find(self, name) -> Dict:
        self.search_attribute["name"] = name

        return {
            "type": "User",
            "count": len(self.search_attribute),
            "attributes": {"username": 'test_22', "full_name": f'Test {self.search_attribute["name"]} Teta', "password": 'testing123'}
        }
