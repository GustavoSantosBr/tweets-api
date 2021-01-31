from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class FileNotFoundException(FileNotFoundError):
    MESSAGE = "Nenhum arquivo encontrado. Não existe o arquivo ou diretório: {}"

    def __init__(self, file_path: str):
        self.__file_path = file_path
        super().__init__(self.__file_path)

    def get_message(self) -> str:
        return self.MESSAGE.format(self.__file_path)

    def get_code(self) -> int:
        return StatusHttp.NOT_FOUND
