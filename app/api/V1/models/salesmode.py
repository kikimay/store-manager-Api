sales = []
sold_items = []

class SalesModel(object):
    def __init__(self):
        self.sales = sales
        self.sold_items = sold_items

    def create_sale_item(self, product_price, name, quantity, total):
        self.sold_item_id = len(sold_items)+1
        sold_item = {
            "id":self.sold_item_id,                         
            "price":product_price,
            "product_name":name,
            "Quantity":quantity,
            "total":total
            }
        
        sold_items.append(sold_item)

        return sold_items

    def create_sale(self, grand, items):
        self.sale_id = len(sales)+1
        sale= {"sale_id":self.sale_id,
               "grand_total":grand,
               "number_of_items":items
               }

        sales.append(sale)

        return sale


    def retrive_all_sales(self):
        return sales

    def find_specificsale(self,sale_id):
        if len(sales) > 0:
            for sale in sales:
                self.sold_item_id = sale.get('sale_id')
                
                if self.sold_item_id == sale_id:
                    return sale



