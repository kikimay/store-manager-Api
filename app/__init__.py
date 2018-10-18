from flask import Flask


from app.api.V1.views import sales
from app.api.V1.views import products



def create_app(config):
    
    
    
    app = Flask(__name__)
    
    app.url_map.strict_slashes = False
    
    #app.config.from_object(app_config[config])
  #  app.config["TESTING"] = True
  

    from .api.V1.views.sales import sales_blueprint
    app.register_blueprint(sales_blueprint)

    from .api.V1.views.products import products_blueprint
    app.register_blueprint(products_blueprint)


    

    return app















