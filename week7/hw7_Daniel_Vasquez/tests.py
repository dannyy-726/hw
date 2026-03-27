from vehicle import Vehicle, Bike, Car
from complex_numbers import ComplexNumber
from shapes import Rectangle, Circle
from expressions import extract_three_digit_numbers,extract_secure_urls,strip_html_tags,reformat_date



if __name__ == "__main__":
   print("Running tests for HW7:\n")


# Task 1: Vehicle Inheritance
   print("Task 1 Tests:")
   my_car = Car("Tesla","Model S", 2020, is_electric=True)
   my_non_electric_car = Car("Ford", "Mustang", 1965)
   print(my_car)
   print(my_non_electric_car)

   #Demonstrating the driving range method:
   print("Electric Car Driving Range:", my_car.driving_range(50))
   print("Non- Electric Car Driving Range:",my_non_electric_car.driving_range(10))

   #Demonstrating Bike method
   my_bike = Bike("Trek", "Domane", 2019, "road")
   print(my_bike)
   print()

# Task 2: Arithmetic Overloading
   print("Task 2 Tests:")

   a=ComplexNumber(2,3)
   b=ComplexNumber(1,7)
   c=a+b
   d=a*b
   print(c)
   print(d)

   #extra credit
   a=ComplexNumber(2,3)
   b=5
   c=a+b
   print(c)
   print()

# Task 3: Shape Management System
   print("Task 3 Tests:")

   rectangle = Rectangle(length=5,width=10)
   print(rectangle.area())
   print(rectangle.dimensions())

   square = Rectangle(side=5)
   print(square.area())
   print(square.dimensions())

   circle = Circle(radius=7)
   print(circle.area())
   print(circle.dimensions())
   print()

# Task 4: Regex
   print("Task 4 Tests:")

   text = "The codes are 101, 42, 999, and the year is 2024."
   print(f"Input: '{text}'")
   print(f'Output: {extract_three_digit_numbers(text)}')
   print()
   
   text = "Visit our site: https://www.example.com/page-1 or the old one: http://legacy.org/index.html. Local link: file://local/path"
   print(f"Input: '{text}'")
   print(f'Output: {extract_secure_urls(text)}')
   print()

   text = "This is a <b>bold</b> word and an <i>italic</i> phrase, ending with a <p>paragraph tag</p>."
   print(f"Input: '{text}'")
   print(f'Output: {strip_html_tags(text)}')
   print()

   text = "The event is scheduled for 10-25-2025, but the deadline passed on 01-15-2024."
   print(f"Input: '{text}'")
   print(f'Output: {reformat_date(text)}')





