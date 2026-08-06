def sum(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        return "Error: Division by zero"
    else:
        return n1/n2


while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice=int(input("Enter your choice: "))
    if choice==5:
        print("Exiting the calculator.")
        break

    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))
        
    if choice==1:
        print("Sum:", sum(n1,n2))
    elif choice==2:
        print("Subtraction:", sub(n1,n2))
    elif choice==3:
        print("Multiplication:", mul(n1,n2))
    elif choice==4:
        print("Division:", div(n1,n2))
    else:
        print("Invalid choice")

