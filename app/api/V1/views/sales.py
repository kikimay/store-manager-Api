from flask import Flask, Blueprint,request,jsonify,make_response
from .products import Products

sales_blueprint = Blueprint('sales', __name__,url_prefix='/api/v1')

  
sales = []#a list of of dictionaries.
sold_items = []#a list of sold items

class Sales(object):
    @sales_blueprint.route("/make_sale", methods=["POST", "GET"])
    def make_sale():
       

        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","message":"request not json"}),400)#data must be json 
        else:
            data = request.get_json() 
            sale_id =  len(sales)+1
           
            order_items = data['order_items']
            attendant_name = data['attendant_name']

            items = Products()
            products = items.stock()
            
            
        if not len(order_items) == 0:
            for order_item in order_items:
                name = order_item.get('name')
                quantity = order_item.get('quantity')   
                    
                    
                    
                if quantity == "":
                    return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                if name == "":
                    return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
                if not quantity.isdigit():
                    return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)
                if not name.isalpha():
                    return make_response(jsonify({"status":"not acceptable", "message":"product name is not valid"}),400)
                        

                for product in products:
                    product_name = product.get('name')
                    product_price = product.get('price')

                    if product_name == name:
                        total = int(quantity) * int(product_price)
                        sold_item = {                               
                            "price":product_price,
                            "product_name":name,
                            "Quantity":quantity,
                            "total":total
                        }
                            

                        sold_items.append(sold_item)
                    else:
                        return make_response(jsonify({"status":"not found","message":"product you are looking for does not exist"}),404)
                   

                grand = 0
                items = 0
                for sold_item in sold_items:
                    I = sold_item.get('sale_id')
                    
                    if I == sale_id:
                        num = sold_item.get('Quantity')
                        total = sold_item.get('total')
                        grand = grand + int(total)
                        items = items + int(num)

            sale= {
                "sale_id":sale_id,
                "attendant_name": attendant_name,   
                "grand_total":grand,
                "number_of_items":items
                }

            sales.append(sale)           
            return make_response(jsonify({"status":"created"}),201)
        else:
            return make_response(jsonify({"status":"not acceptable", "message":"You must add atleast one item"}),406)
 


            
            
    @sales_blueprint.route("/sales", methods=["GET"])
    def salesall():
        
        if len(sales) == 0:
            return make_response(jsonify({"status":"not found","message":"sale you are looking for does not exist"}),404)
                   
        else:
            return make_response(jsonify({"status":"ok", "sales":sales}),200)
        


    @sales_blueprint.route('/sales/<int:sale_id>', methods=['GET'])
    def specificsale(sale_id):
        
        sale = [sale for sale in sales if sale.get('sale_id')==sale_id]
        
        
        if len(sales) == 0:
            return make_response(jsonify({"status":"not found","message":"sale you are looking for does not exist"}),404)
                   
        else:
            return make_response(jsonify({"status":"ok", "sale":sale}),200)

