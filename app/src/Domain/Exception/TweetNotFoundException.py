from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class TweetNotFoundException(Exception):

    def __init__(self, message: str = "Nenhum resultado encontrado."):
        self.__message = message
        super().__init__(self.__message)

    def get_message(self) -> str:
        return self.__message

    def get_code(self) -> int:
        return StatusHttp.NOT_FOUND
