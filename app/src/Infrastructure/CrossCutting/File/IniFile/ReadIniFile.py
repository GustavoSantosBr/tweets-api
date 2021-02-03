from configparser import ConfigParser

from src.Infrastructure.CrossCutting.File.BaseFile import BaseFile


class ReadIniFile(BaseFile):

    def read_file(self, file_path: str = "config.ini") -> ConfigParser:
        config = ConfigParser()
        config.read(file_path)
        return config
