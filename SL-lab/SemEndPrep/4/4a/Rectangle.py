class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate(self):
        print("Area = ",(self.l*self.b))
    
r = Rectangle(10,120)
r.calculate()