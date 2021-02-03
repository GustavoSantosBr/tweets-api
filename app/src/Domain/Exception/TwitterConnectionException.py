from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class TwitterConnectionException(Exception):

    def __init__(self, message: str = "Não foi possível realizar a conexão com a API do Twitter."):
        self.__message = message
        super().__init__(self.__message)

    def get_message(self) -> str:
        return self.__message

    def get_code(self) -> int:
        return StatusHttp.INTERNAL_SERVER_ERROR
