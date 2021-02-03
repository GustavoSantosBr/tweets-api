from unittest import main, TestCase
from unittest.mock import patch

from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class TestGetTweetsByUserNameHandler(TestCase):
    TARGET = "src.Application.Handler.GetTweetsByUserNameHandler"

    def test_get_method_when_successfully_executed(self):
        with patch(self.TARGET) as mock_get:
            mock_get.return_value.status_code.return_value = StatusHttp.OK
        assert mock_get.return_value.status_code.return_value == StatusHttp.OK


if __name__ == "__main__":
    main()
