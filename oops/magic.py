from rect import Rectangle
num1=22
num2=21

t= num1 + num2
print(t)

r1=Rectangle(5, 10)
r2=Rectangle(7, 3)
r3=Rectangle(0, 0)

r3 = r1 + r2
print(r1)
print(r2)
print(r3)

if(r1>=r2):
    print(f"{r1} is greater than {r2}")
else:
    print(f"{r2} is greater than {r1}")