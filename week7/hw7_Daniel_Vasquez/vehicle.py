class Vehicle:
    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type:str):
        super().__init__(make, model, year)
        if bike_type not in ["road","mountain"]:
            raise ValueError ('bike_type must be either "road" or "mountain"')
        self.bike_type = bike_type
    
    def __str__(self):
        return f"{super().__str__()}, {self.bike_type} type"
    
class Car(Vehicle):
    def __init__(self, make, model, year, is_electric=False,miles_per_battery_percent=4, miles_per_gallon=30):
        super().__init__(make, model, year)

        self.is_electric = is_electric
        self.miles_per_battery_percent = miles_per_battery_percent
        self.miles_per_gallon = miles_per_gallon    
    
    def driving_range(self,energy:float):
        if self.is_electric:
            if energy < 0 or energy > 100:
                raise ValueError ("Energy must be between 0 - 100")
        else:
            if energy < 0 or energy >=1000:
                raise ValueError("Energy has to be greater than 0 and less than 1000 gallons")           
        
        if self.is_electric:
            range = self.miles_per_battery_percent * energy
        else:
            range = self.miles_per_gallon * energy
        return range 
    
    def __str__(self):
        if self.is_electric:
            return f"{super().__str__()}, Electric"
        else:
            return f"{super().__str__()}, Non-Electric"
        
        

    
        