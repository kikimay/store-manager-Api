
products = []


class ProductsModel(object):
    def __init__(self):
        self.products = products

    def create_item(self, name, price, image,quantity):
        self.product_id = len(products)+1
        product= {
            "product_id":self.product_id,
            "name":name,
            "price":price,   
            "image":image,
            "quantity":quantity 
            }
        products.append(product)

        return product

    def retrive_all_products(self):
        return products

    def find_product_by_name_and_price(self, name, price):
        if len(products) > 0:
            for product in products:
                self.product_name= product.get('name')
                self.product_price = product.get('price')
                if name == self.product_name and price == self.product_price:
                    return product


    def find_product_by_id(self,product_id):
        if len(products) > 0:
            for product in products:
                self.id= product.get('product_id')
                    
                if self.id == product_id:
                    return product


