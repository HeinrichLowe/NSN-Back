from src.presentation.controllers.users.register import RegisterController
from src.data.tests.register_spy import RegisterSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self):
        self.body = {
            "user": {
                "email": "testkappa@gmail.com",
                "username": "test_kappa",
                "password": "test123",
                "full_name": "Test Twenty Three",
                "avatar": None,
                "birthday": None,
            }
        }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = RegisterSpy()
    search_by_name = RegisterController(use_case)

    response = search_by_name.handle(http_request_mock)

    #print('\n\n', vars(response), '\n\n')

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
