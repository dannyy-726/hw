from product_inventory import Product

class Shopper:
    def __init__(self,name:str, shopper_id:str):
        
        self.name = name
        self.shopper_id = shopper_id
        self.cart = {} 
    
    def add_item(self,product: Product,quantity: int):
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0.")
        
        product.sell_product(quantity)

        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_item(self, product: Product, quantity: int):

        if product not in self.cart:
            return
        current_quantity = self.cart[product]

        if quantity >= current_quantity:
            product.add_stock(current_quantity)
            self.cart.pop(product)
        else:
            product.add_stock(quantity)
            self.cart[product] -= quantity

    def cart_total(self):
        total = 0.00
        for product, quantity in self.cart.items():
            total += product.price * quantity
        return round(total, 2)

class PremiumShopper(Shopper):
        def cart_total(self):
            total = super().cart_total()
        
            if total >= 50:
                total *= 0.965

            return round(total, 2)


