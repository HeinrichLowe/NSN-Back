from src.domain.use_cases.user.get_basic_user_info import IGetBasicUserInfo
from src.presentation.http_types import HttpResponse

class GetBasicUserInfoController():
    def __init__(self, use_case: IGetBasicUserInfo):
        self.__use_case = use_case

    async def handle(self, user_id: str) -> HttpResponse:
        response = await self.__use_case.execute(user_id)
        return HttpResponse(status_code=200, body=response)
