from vehicle import Vehicle
from library import LibraryMember
from product_inventory import Product
from shopper import Shopper, PremiumShopper

if __name__ == "__main__":
    print("Running test for HW6:\n")


    # Task 1: Vehicle
    print("Task 1: Vehicle")
    car = Vehicle("Vin123", "Toyota", "Camry", 2020)
    #car2 = Vehicle("VIN456", "Tesla", "Model", 2026) #should return Value error for year
    print(car)
    #print(car2)
    print()

    #Task 2: LibraryMember
    print("Task 2: LibraryMember")
    member = LibraryMember("001", "Alice")
    member.add_book("The Great Gatsby")
    print(member)

    #check to see if you can add the same book twice
    #member.add_book("The Great Gatsby")
    #check if you can remove a book that is not checked out
    #member.remove_book("Harry Potter")
    print()

    #Task 3: Product
    print("Task 3: Product")
    product = Product("12345", "Coffee Mug", 12.99, 100)
    product.sell_product(2)
    print(product)

    product.update_price(7.99)
    print(product)

    product.add_stock(50)
    print(product)

    #try adding negative stock
    #product.add_stock(-100)

    #try selling more than the quantity given
    #product.sell_product(100)
    print()

    #Task 4: Shopper
    print("Task 4: Shopper")
    mug = Product("111", "Mug", 10.00, 10)
    shopper = Shopper("Bob", "S001")
    shopper.add_item(mug, 3)
    print(f"Cart total: ${shopper.cart_total():.2f}")
    print(f"Remaining stock: {mug.quantity_available}")

    #Try adding more than is available in stock
    #shopper.add_item(mug,10)
    print()

    #Task 4: PremiumShopper
    print("Task 4: PremiumShopper")
    laptop = Product("222", "Laptop Bag", 30.00, 10)
    premium = PremiumShopper("Daniel", "P001")
    premium.add_item(laptop, 2)
    print(f"Cart total (with discount if applicable): ${premium.cart_total():.2f}")
    print(f"Remaining stock: {laptop.quantity_available}") 

    #try adding more stock than available
    #premium.add_item(laptop,10)
