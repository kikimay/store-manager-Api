from flask import Flask, Blueprint,request,jsonify,make_response
from .products import Products
from app.api.V1.utils.validators import  json_check, quantity_checker, name_checker, price_checker, image_checker
from app.api.V1.models.items import products
from app.api.V1.models.salesmode import SalesModel,sold_items,sales
sales_blueprint = Blueprint('sales', __name__,url_prefix='/api/v1')

class Sales(object):
    @sales_blueprint.route("/make_sale", methods=["POST", "GET"])
    def make_sale():
        json_check(request)
        data = request.get_json() 
        order_items = data['order_items']
      
        items = Products()
       
        if len(order_items) != 0:
            for order_item in order_items:
                name = order_item.get('name')
                quantity = order_item.get('quantity')   
                quantity_checker(quantity)
                name_checker(name)        

                for product in products:
                    product_name = product.get('name')
                    product_price = product.get('price')
                   

                    if product_name == name:
                        total = int(quantity) * int(product_price)
                        sales_model = SalesModel()
                        sale_item = sales_model.create_sale_item(product_price, name, quantity, total)
                        print(sale_item)
                '''else:
                    return make_response(jsonify({"status":"not found","message":"product you are looking for does not exist"}),404)
                '''

            grand = 0
            items = 0
            for sold_item in sold_items:
                I = sold_item.get('sale_id')
                sale_id = len(sales)+ 1
                if I == sale_id:
                    num = sold_item.get('Quantity')
                    total = sold_item.get('total')
                    grand = grand + int(total)
                    items = items + int(num)
                    
            sale = SalesModel().create_sale(grand, items)
            if sale:        
                return make_response(jsonify({"status":"created","sale":sale}),201)
        else:
            return make_response(jsonify({"status":"not acceptable", "message":"You must add atleast one item"}),406)
 
    @sales_blueprint.route("/sales", methods=["GET"])
    def salesall():
        # if not sales:
        if len(sales) == 0:
            return make_response(jsonify({"status":"not found","message":"sale you are looking for does not exist"}),404)
                   
        else:
            return make_response(jsonify({"status":"ok", "sales":sales}),200)
        
    @sales_blueprint.route("/sales/<int:sale_id>", methods=['GET'])
    def specificsale(sale_id):
        sale = [sale for sale in sales if sale.get('sale_id')==sale_id]
        if len(sales) == 0:
            return make_response(jsonify({"status":"not found","message":"sale you are looking for does not esxist"}),404)
        else:
            return make_response(jsonify({"status":"ok", "sale":sale}),200)
            



    
       