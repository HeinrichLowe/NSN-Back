from abc import ABC, abstractmethod
from src.presentation.http_types import HttpRequest, HttpResponse

@abstractmethod
class IController(ABC):
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
