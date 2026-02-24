import sys
class Vehicle:
    def __init__(self,vehicle_id:str,make:str,model:str,year:int):

        if year < 1900 or year > 2025:
            raise TypeError("year must be between 1900 and 2025")
        
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"Vehicle(vehicle_id='{self.vehicle_id}', make='{self.make}', model='{self.model}', year={self.year})"
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise ValueError("Usage: python vehicle.py ,<vehicle_id> <make> <model> <year>")
    
    vehicle_id = sys.argv[1]
    make = sys.argv[2]
    model = sys.argv[3]

    try:
        year = int(sys.argv[4])
    except ValueError:
        raise TypeError("year must be an integer")
    
    vehicle = Vehicle(vehicle_id,make,model,year)
    print(vehicle)
    
    
