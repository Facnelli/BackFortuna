from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        user_name = request.query_params['user_name']

        response = self.__use_case.find(user_name)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )