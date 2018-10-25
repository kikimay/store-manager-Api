from flask import jsonify,request,make_response,json, abort


def json_check(request):
    if not request.is_json:
        abort (make_response(jsonify({"status":"wrong format","messenge":"request not json"}),400))

def quantity_checker(quantity):
    if quantity == "":
        return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
    if not quantity.isdigit():
        return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)

def name_checker(name):
    if name == "":
        return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
    if not name.isalpha():
        return make_response(jsonify({"status":"not acceptable", "message":"product name is not valid"}),400)

def price_checker(price):
    if price == "":
        return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
    if not price.isdigit():
        return make_response(jsonify({"status":"not acceptable", "message":"price is not valid"}),400)
      
def image_checker(image):
    if image == "":
        return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)

                