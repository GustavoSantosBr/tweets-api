from typing import Tuple

import pandas

from src.Domain.Exception.FileNotFoundException import FileNotFoundException
from src.Infrastructure.CrossCutting.File.BaseFile import BaseFile
from src.Infrastructure.CrossCutting.File.CsvFile.ReadCsvFile import ReadCsvFile


class UpdateCsvFile(BaseFile):

    def __init__(self):
        self.__read_csv_file = ReadCsvFile()

    def insert_or_update_file(self, file_name: str, data: list) -> Tuple[int, int]:
        try:
            file_path = f"{file_name}_tweets.csv"
            data_in_data_frame = pandas.DataFrame(data)

            if self.file_exists(file_path):
                old_records = self.__read_csv_file.read_file(file_path)
                all_records = pandas.concat([old_records, data_in_data_frame])
                new_records = all_records.drop_duplicates(subset=["id"], keep="last", inplace=False)
                count_all_records = new_records.shape[0]

                new_records.to_csv(file_path, index=False)
                return count_all_records - old_records.shape[0], count_all_records

            count_new = data_in_data_frame.shape[0]
            new_records = pandas.DataFrame().append(data_in_data_frame)
            new_records.to_csv(file_path, index=False)
            return count_new, count_new

        except FileNotFoundError as e:
            raise FileNotFoundException(e.filename)
