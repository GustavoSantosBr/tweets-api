import pandas
from pandas import DataFrame

from src.Domain.Exception.FileNotFoundException import FileNotFoundException
from src.Infrastructure.CrossCutting.File.BaseFile import BaseFile


class ReadCsvFile(BaseFile):

    def read_file(self, file_path: str) -> DataFrame:
        if self.file_exists(file_path):
            return pandas.read_csv(file_path)
        raise FileNotFoundException(file_path)
