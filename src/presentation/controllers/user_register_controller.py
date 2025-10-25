from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface


class UserRegisterController(ControllerInterface):
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:

        user_name = request.body["user_name"]
        email = request.body["email"]
        password = request.body["password"]

        response = self.__use_case.register(user_name, email, password)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )