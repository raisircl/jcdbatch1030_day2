class Quadilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    