from flask import Flask, Blueprint



products_blueprint = Blueprint('products', __name__,url_prefix='/api/v1')


class Products(object):
    pass
