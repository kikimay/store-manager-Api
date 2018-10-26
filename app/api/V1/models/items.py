
products = []


class ProductsModel(object):
    def __init__(self,name,price,image,quantity):
        self.product_id = len(products)+1
        self.products = products
        self.name = name
        self.price = price
        self.image = image
        self.quantity = quantity

    
    def add_item(self):
        product_dict= {
            "product_id":self.product_id,
            "name":self.name,
            "price":self.price,   
            "image":self.image,
            "quantity":self.quantity 
            }
        products.append(product_dict)

        return product_dict
   
    def find_product_by_name_and_price(self, name, price):
        if len(products) > 0:
            for product in products:
                self.product_name= product.get('name')
                self.product_price = product.get('price')
                if name == self.product_name and price == self.product_price:
                    return product


          


    