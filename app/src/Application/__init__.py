from flask import Flask
from flask_restful import Api

from src.Application import Routes

app: Flask = Flask(__name__)

application = Api(app)
Routes.add_routes(application)
