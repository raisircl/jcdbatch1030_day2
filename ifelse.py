'''
Decision control instructions: as we know a program is a
solution of problem and a problem can not solve wihtout 
decision so to take decision in in python program there are
folowing decision control instructions:
1. if else statement
syntax of if else statement:

if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False     

'''
# enter mrp of a book and and 10 % discount 
# if mrp is >= 1000 otherwise 5% discount
mrp=float(input("Enter mrp of book: "))
discount=0
if mrp>=1000:
    discount=mrp*10/100
else:
    discount=mrp*5/100

net=mrp-discount
print(f"mrp = {mrp} and discount = {discount} and net price ={net}")

# enter sale price and cost price of a product and find profit or loss
# enter 2 nos and print which one is greater
# enter a number and print whether it is even or odd
# enter a number and print whether it is positive or negative

