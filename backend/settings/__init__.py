from flask import Flask, request, g, Response
from flask_cors import CORS
from .settings import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_json_schema import JsonSchema
from flask_restful import Resource, Api
from apps.todo_list.v1.urls import todo_list_router
import os


# App register section
enviroment:str = os.getenv('FLASK_ENV')
_app = Flask(__name__)
#_app.config.from_object(app_config[enviroment])

# Api config 
_api = Api(_app)


    
# Define database 
_db = SQLAlchemy(_app)


def get_app():
    """ Return app instance """
    return _app

def get_api():
    """ Return api """
    return _api

def get_db():
    """ Return db instance """
    return _db

def settings():
    """ Create the app config """

    # Cords Settings App 
    CORS(_app)

    # validate JSON data 
    JsonSchema(_app)

    todo_list_router(_app)

    return _app


