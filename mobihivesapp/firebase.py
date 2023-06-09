import pyrebase
from mobihivesproj.config_keys import config


def firebase_config():
    firebase = pyrebase.initialize_app(config)
    authe = firebase.auth()
    database = firebase.database()
    return database