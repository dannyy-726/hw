import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class Rectangle(Shape):
    def __init__(self, length=None, width=None, side=None):
        if side is not None and length is None and width is None:
            self.side = side
            self.length = None
            self.width = None

        elif side is None and length is not None and width is not None:
            self.side = None
            self.length = length
            self.width = width

        else:
            raise ValueError("Provide either length and width OR side")
    def area(self):
        if self.side is not None:
            return self.side * self.side
        return self.length * self.width
    
    def dimensions(self):
        if self.side is not None:
            return {'side': self.side}
        return {'length':self.length, 'width': self.width}
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * (self.radius ** 2),2)
    
    def dimensions(self):
        return {'radius':self.radius}
    

         
                 

