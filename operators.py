# Operator - It is a special symbol which is used to operates on data. 
# The data on which operators operate is called operands. 
# eg. 5+7 here 5 and 7 are operands and + is an operator.
# Unary Operator - Operator which operates on single operand 
# is called unary operator. eg. +5, -7 etc
# Binary Operator - Operator which operates on two operands 
# is called binary operator. eg. 5+7, 8*9, 5>2 etc
# Binary operators are further classified into following types:
# Arithmetic Operators - These operators are used to 
# perform arithmetic operations like 
# addition +, subtraction -, multiplication *, division /, 
# modulus %, exponentiation **, floor division //
# Comparison Operators - These operators are used to compare two values.
# They return either True or False.
# <, >, <=, >=, ==, !=
# Logical Operators - These operators are used to combine conditional statements.
# and, or, not
# Priority of Operators - Which one operator operate first
# Associativity of Operators - operators has same priority then which one operate first
# 6*2/4 => 3 
# 6/2*4 =>12
x=6*2/4
y=6/2*4
print(f"x = {x} and y = {y}")

age=10

result=age>18 or age<30
print(result)
