from quadilateral import Quadilateral

class Rectangle(Quadilateral): # parent class is Quadilateral its constructor is called using super() function 
    def __init__(self, length, breadth):
        super().__init__(length, breadth, length, breadth)
        self.length = length
        self.breadth = breadth

    def area(self):
        print("I am area of Rectangle")
        return self.length * self.breadth