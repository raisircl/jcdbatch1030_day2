class person:
    count=0 # class attribute
    def __init__(self, name="unknown", age=0):
        person.count += 1 # incrementing the class attribute
        self.uuid=person.count # instance attribute
        self.name=name # instance attribute
        self.age=age # instance attribute
    def display(self):
        print(f"UUID: {self.uuid}, Name : {self.name} Age: {self.age}")

p1=person()
p1.name="John"
p1.age=25

p2=person("Alice", 30)

p1.display()
p2.display()

# Create a Rect class with Length and Breadth
# create a display, are method

# Box - l, b, h , methos - display, area, volume

# Circle - r, methods - display, area, circumference

# BankAccount - 
# Instance attributes - accno, name, balance
# methods - display, deposit, withdraw
# accno should be auto generated and start from 1001
# take a class attrribute x intialize it with 1000

