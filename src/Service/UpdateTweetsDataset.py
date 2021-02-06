from datetime import datetime

from src.Domain.DTO.ParametersDto import ParametersDto
from src.Domain.DTO.TweetDatasetDto import TweetDatasetDto
from src.Infrastructure.CrossCutting.File.CsvFile.UpdateCsvFile import UpdateCsvFile
from src.Service.GetTweets import GetTweets


class UpdateTweetsDataset:

    def __init__(self):
        self.__get_tweets = GetTweets()
        self.__update_csv_file = UpdateCsvFile()

    def update_tweets_dataset_by_user_name(self, parameters: ParametersDto) -> TweetDatasetDto:
        tweets = self.__get_tweets.get_tweets_by_user_name(parameters)
        user_name = parameters.name
        update_file = self.__update_csv_file.insert_or_update_file(user_name, tweets.to_table())
        return TweetDatasetDto(datetime.now(), update_file[0], update_file[1])
