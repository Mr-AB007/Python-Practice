#Program to use single inheritance where base class claculate area of Square and child cal Area of Rectangle
    def __init__(self,side):
        self.side = side
    # to calculaate area 
    def area(self):
        return self.side * self.side
# derived class

class Rectangle(Square):
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    #overiding the area method
    def area(self):
        return self.breadth*self.length

#drive code

obj = Square(5)
print("Area of Square %d"%(obj.area()))

#derived class oject rectangle

obj = Rectangle(5,3)
print("Area of Rectangle %d"%(obj.area()))
class Square:
def __init__(self,side):
        self.side = side
    # to calculaate area 
    def area(self):
        return self.side * self.side
# derived class

class Rectangle(Square):
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    #overiding the area method
    def area(self):
        return self.breadth*self.length

#drive code

obj = Square(5)
print("Area of Square %d"%(obj.area()))

#derived class oject rectangle

obj = Rectangle(5,3)
print("Area of Rectangle %d"%(obj.area()))
