from quadilateral import Quadilateral

class Rectangle(Quadilateral): # parent class is Quadilateral its constructor is called using super() function 
    count = 0
    def __init__(self, length, breadth):
        Rectangle.count += 1
        super().__init__(length, breadth, length, breadth)
        self.id=Rectangle.count
        self.length = length
        self.breadth = breadth

    def area(self):
        print("I am area of Rectangle")
        return self.length * self.breadth
    def __add__(self,r):
        print("I am add method of Rectangle")
        temp=Rectangle(0,0)
        temp.length = self.length + r.length
        temp.breadth = self.breadth + r.breadth
        return temp
    def __ge__(self,r):
        print("I am ge method of Rectangle")
        return self.area() >= r.area()

    def __str__(self):
        return f"Rect{self.id} Dimension is {self.length}x{self.breadth}"

#r2+r1