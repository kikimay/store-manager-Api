from flask import Flask, Blueprint,request,jsonify,make_response


sales_blueprint = Blueprint('sales', __name__,url_prefix='/api/v1')



    
sales = []
sale_items = []

class sales(object):
    @sales_blueprint.route("/make_sale", methods=["POST", "GET"])
    def make_sale():
       

        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","message":"request not json"}),400)#data must be json 
        else:
            data = request.get_json() 
            sale_id =  len(sales)+1
            added_by = added_by['user_id']
            sold_items = data['sale_items']
            total_paid = data['total_paid']
            
            

            
           
        if total_paid == "" or sold_items == "" :
            return make_response(jsonify({"status":"not acceptable","message":"You must fill all fields"}),406)

        
        else:
            if len(sale_items) != 0:
                for sale_item in sale_items:
                    product_name = sale_item.get('product_name')
                    quantity = sale_item.get('quantity')
                    
                    sale_item_id =  len(sale_items)+1
                    
                    if quantity == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    if product_name == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
                    if not quantity.isdigit():
                        return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)
                    if not product_name.isalpha():
                        return make_response(jsonify({"status":"not acceptable", "message":"product name is not valid"}),400)
                        

                    for product in products:
                        name = product.get('name')
                        price = product.get('price')

                        if product_name == name:
                            total = int(quantity) * int(price)
                            sale_item = {
                                "sale_item_id":sale_item_id,
                                "sale_id":sale_id,
                                "product_name":product_name,
                                "Quantity":quantity,
                                "price":price,
                                "total":total
                                }
                            

                            sale_items.append(sale_item)

                    grand = 0
                    items = 0
                    for sale_item in sale_items:
                        I = sale_item.get('sale_id')
                        
                        if I == sale_id:
                            num = sale_item.get('Quantity')
                            total = sale_item.get('total')
                            grand = grand + int(total)
                            items = items + int(num)

                order = {
                    "sale_id":sale_id,
                    "ordered_by":ordered_by,
                    "added_by":added_by,   
                    "total_paid":total_paid,
                    
                    "grand_total":grand,
                    "number_of_items":items
                    }

                sales.append(sale)           
                return make_response(jsonify({"status":"created", "sales":sales, "sale_items":sale_items, "saler":sale, "sale_item":sale_item,}),201)
            else:
                return make_response(jsonify({"status":"not acceptable", "message":"You must add atleast one item"}),406)
