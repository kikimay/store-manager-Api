from flask import Flask, Blueprint,request,jsonify,make_response
#from app import create_app


products_blueprint = Blueprint('products', __name__,url_prefix='/api/v1')

products = []

class Products(object):
    @products_blueprint.route("/products", methods=["POST"])
    def add_product(): #define a method that adds new product item
        
        
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","messenge":"request not json"}),400)
        else:
            data = request.get_json() 
            product_id =  len(products)+1
            name = data['name']
            price = data['price']
            image = data['image']
            

        if name == "" or price == "" or image == "":
            return make_response(jsonify({"status":"not acceptable","message":"all fields must be filled"}),406)

        if not price.isdigit():
            return make_response(jsonify({"status":"not acceptable","message":"price not valid"}),404)

        if not name.isalpha():
            return make_response(jsonify({"status":"not acceptable","message":"product name not valid"}),405)

        
        

        if len(products) > 0:
            for product in products:
                product_name= product.get('name')
                product_price = product.get('price')#for every product item in the list of products get its price an name
                
            if name == product_name and price == product_price:
                return make_response(jsonify({"status":"forbidden","message":"product already exists"}),403)
           
            else:#if the product does not exist add the new product item
                product= {
                    "product_id":product_id,
                    "name":name,
                    "price":price,   
                    "image":image,
                   
                    }

                
                
        else:#if the list of products is empty add the new product item
            product = {
                 "product_id":product_id,
                 "name":name,
                 "price":price,   
                 "image":image,
                
                 }

        products.append(product)

        return make_response(jsonify({"status":"created", "product":product, "products":products }),201)


    @products_blueprint.route("/api/v1/products", methods=["GET"])
    def productsall(): #a function that returns all products available
        if len(products) == 0:
            return make_response(jsonify({"status":"not found","message":"products you are looking for does not esxist"}),404)
        else:
            return make_response(jsonify({"status":"ok", "products":products}),200)


    
