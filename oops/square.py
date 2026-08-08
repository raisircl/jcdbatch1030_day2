from rect import Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
            print("I am area of Square")
            return self.side ** 2