from flask import request, Response
from flask_restful import Resource

from src.Domain.DTO.ParametersDto import ParametersDto
from src.Domain.Exception.FileNotFoundException import FileNotFoundException
from src.Domain.Exception.TweetNotFoundException import TweetNotFoundException
from src.Domain.Exception.TwitterConnectionException import TwitterConnectionException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Service.UpdateTweetsDataset import UpdateTweetsDataset


class UpdateTweetsDatasetHandler(Resource):

    def put(self, name: str) -> Response:
        try:
            parameters = ParametersDto(name, request.args)
            update_tweets_dataset = UpdateTweetsDataset()
            result = update_tweets_dataset.update_tweets_dataset_by_user_name(parameters)
            return ResponseApi(result, StatusHttp.OK).response()
        except TweetNotFoundException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except TwitterConnectionException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except FileNotFoundException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except Exception as e:
            return ResponseApi(e.args).response()
