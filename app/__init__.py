# app/__init__.py

from flask import Flask
from app.tests.v1 import test_products
from app.tests.v1 import test_sales


# local import
from instance.config import app_config

# initialize sql-alchemy
#db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    return app
