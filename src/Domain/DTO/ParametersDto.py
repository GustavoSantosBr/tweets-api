class ParametersDto:
    LIMIT = 10

    def __init__(self, name: str, request: dict):
        self.__name = name
        self.__limit = request.get("limit")
        self.__date_since = request.get("since")

    @property
    def name(self):
        return self.__name.strip()

    @property
    def limit(self) -> int:
        limit = self.__limit

        if limit is None:
            return self.LIMIT
        return int(limit)

    @property
    def date_since(self) -> str or None:
        return self.__date_since
