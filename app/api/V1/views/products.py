from flask import Flask, Blueprint,request,jsonify,make_response
from app.api.V1.models.items import products
from app.api.V1.models.items import ProductsModel
from app.api.V1.utils.validators import  json_check, quantity_checker, name_checker, price_checker, image_checker


products_blueprint = Blueprint('products', __name__,url_prefix='/api/v1')


class Products(object):
    @products_blueprint.route("/products", methods=["POST"])
    def add_product(): 
        
        
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","messenge":"request not json"}),400)
        data = request.get_json() 
        name = data['name']
        price = data['price']
        image = data['image']
        quantity = data['quantity']
        
        
       
        if quantity == "":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
        if not quantity.isdigit():
            return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)
        if name == "":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
        if not name.isalpha():
            return make_response(jsonify({"status":"not acceptable", "message":"product name is not valid"}),400)
        if price == "":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
        if not price.isdigit():
            return make_response(jsonify({"status":"not acceptable", "message":"price is not valid"}),400)
        if image == "":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)

        products_model = ProductsModel(name,price,image,quantity)
        product = products_model.find_product_by_name_and_price(name, price)
       
        if product:
            return make_response(jsonify({"status":"forbidden","message":"product already exists"}),403)
           
        else:
            product= ProductsModel(name,price,image,quantity )
            item = products_model.add_item()
            
            return make_response(jsonify({"status":"created", "product":item, "products":products}),201)



    @products_blueprint.route("/products", methods=["GET"])
    def productsall(): 
       
        if len(products) == 0:
            return make_response(jsonify({"status":"not found","message":"products you are looking for does not esxist"}),404)
        else:
            return make_response(jsonify({"status":"ok", "products":products}),200)

    

    @products_blueprint.route('/products/<int:product_id>', methods=["GET"])
    def specificproduct(product_id):
        product = [product for product in products if product.get('product_id')==product_id]
        if len(products) == 0:
            return make_response(jsonify({"status":"not found","message":"product you are looking for does not esxist"}),404)
        else:
            return make_response(jsonify({"status":"ok", "product":product}),200)
            







































































































