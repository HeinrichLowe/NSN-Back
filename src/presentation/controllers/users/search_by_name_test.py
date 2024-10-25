from src.presentation.controllers.users.search_by_name import SearchByNameController
from src.data.tests.search_by_name_spy import SearchByNameSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self):
        self.query_params = { "name": "Testing" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = SearchByNameSpy()
    search_by_name = SearchByNameController(use_case)

    response = search_by_name.handle(http_request_mock)

    #print('\n\n', vars(response), '\n\n')

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
