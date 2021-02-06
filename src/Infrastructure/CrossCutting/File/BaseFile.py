from os.path import exists


class BaseFile:

    def __init__(self):
        pass

    def file_exists(self, file_path: str) -> bool:
        return exists(file_path)
