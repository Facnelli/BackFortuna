from .user_register_controller import UserRegisterController
from src.data.tests.user_register_spy import UserRegisterSpy
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "user_name": "test_user",
            "email": "test@example.com",
            "password": "123456"
        }


def test_handle():
    # Arrange
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    controller = UserRegisterController(use_case)

    # Act
    response = controller.handle(http_request_mock)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert "data" in response.body
    assert response.body["data"]["user_name"] == "test_user"
    assert response.body["data"]["email"] == "test@example.com"

    # Verifica se o use case foi chamado corretamente
    assert use_case.was_called is True
    assert use_case.user_name == "test_user"
    assert use_case.email == "test@example.com"
    assert use_case.password == "123456"
