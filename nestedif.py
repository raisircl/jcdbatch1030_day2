'''
Nested if statements: A nested if statement is an if statement
inside another if statement. It allows you to check multiple
conditions in a hierarchical manner.
Syntax:

if condition1:
    if condition2:
        # code to execute if both condition1 and condition2 are True
    else:
        # code to execute if condition1 is True and condition2 is False
else:
    if condition3:
        # code to execute if condition1 is False and condition3 is True
    else:
        # code to execute if both condition1 and condition3 are False
    
'''
# enter age of a person and check lic eligibility
# criteria age between 18 to 45
age=int(input("Enter age of person: "))
# 20, 10, 50
if age>=18:
    if age<=45:
        print("Eligible for LIC")
    else:
        print("Not eligible for LIC")
else:
    print("Not eligible for LIC")

# enter age of ram , sham and mohan and print who is eldest
# biggest between 3 nos
