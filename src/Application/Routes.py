from flask_restful import Api

from src.Application.Handler.GetTweetsByUserNameHandler import GetTweetsByUserNameHandler
from src.Application.Handler.UpdateTweetsDatasetHandler import UpdateTweetsDatasetHandler


def add_routes(application: Api):
    application.add_resource(GetTweetsByUserNameHandler, "/tweets/<name>")
    application.add_resource(UpdateTweetsDatasetHandler, "/tweets/<name>/csv")
