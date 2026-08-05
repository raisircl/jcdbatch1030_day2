# when a function calls itself, it is called recursion
def fact(num): #5, 4, 3, 2, 1
    if num==1:
        return 1
    else:
        return num * fact(num-1)
              # 5  * 24
              # 4  * 6
              # 3  * 2
              # 2  * 1 
f=fact(5) # 120
print(f)

# sum of n natural numbers using recursion
