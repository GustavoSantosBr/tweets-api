import tweepy
from tweepy import API

from src.Infrastructure.CrossCutting.File.IniFile.ReadIniFile import ReadIniFile


class TwitterConnection:

    @staticmethod
    def connect() -> API:
        read_ini_file = ReadIniFile()
        config = read_ini_file.read_file()
        return tweepy.API(tweepy.OAuthHandler(
            config.get("TWITTER", "API_KEY"),
            config.get("TWITTER", "API_SECRET")), wait_on_rate_limit=True)
