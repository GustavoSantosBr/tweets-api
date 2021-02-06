from flask import request, Response
from flask_restful import Resource

from src.Domain.DTO.ParametersDto import ParametersDto
from src.Domain.Exception.TweetNotFoundException import TweetNotFoundException
from src.Domain.Exception.TwitterConnectionException import TwitterConnectionException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Service.GetTweets import GetTweets


class GetTweetsByUserNameHandler(Resource):

    def __init__(self):
        self.__get_tweets = GetTweets()

    def get(self, name: str) -> Response:
        try:
            parameters = ParametersDto(name, request.args)
            result = self.__get_tweets.get_tweets_by_user_name(parameters)
            return ResponseApi(result, StatusHttp.OK).response()
        except TweetNotFoundException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except TwitterConnectionException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except Exception as e:
            return ResponseApi(e.args).response()
