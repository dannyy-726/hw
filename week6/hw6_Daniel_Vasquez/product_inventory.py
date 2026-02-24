class Product:

    def __init__(self,product_code:str,name:str,price:float,quantity_available:int):
        self.product_code = product_code
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
        else: 
            raise ValueError(f"Sale price must be greater than 0")
        
    def add_stock(self,quantity):
        if quantity > 0:
            self.quantity_available += quantity
        else:
            raise ValueError(f"quantity must be greater than 0")
        
    def sell_product(self,quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > self.quantity_available:
            raise ValueError("Insufficient stock to complete this order")
        else: 
            self.quantity_available -= quantity
        

    def __str__(self):
        return f"Product(product_code='{self.product_code}', name='{self.name}', price={self.price}, quantity_available={self.quantity_available})"
    
    def __repr__(self):
        return self.__str__()