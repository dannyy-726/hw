class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"ComplexNumber with real part {self.real} and imaginary part {self.imaginary}"
    
    def __add__(self,other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        
        if isinstance(other,(int,float)):
            return ComplexNumber(self.real + other, self.imaginary)
        raise TypeError("Operand must be ComplexNumber or a numeric type")
    
    def __mul__(self,other):
        if isinstance(other,ComplexNumber):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real_part,imaginary_part)
       
        # ex. for mult with a int/float. a = Complex(2,3) -> a = 2 + 3i. for mult (2+3i) * 4 
        if isinstance(other,(int,float)):
            return ComplexNumber(self.real * other,self.imaginary * other)
        raise TypeError("Operand must be ComplexNumber or a numeric type")
