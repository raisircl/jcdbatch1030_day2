# range function : generate a sequence of numbers
# for loop use to execute in list, tupple, set, string, dictionary or any sequence
# syntax: for variable in list:
a= range(1,6,2) 
for i in a:
    print(i)

# not like while to intialize the loop counter variable 
# no headache of increment or decrement the loop counter variable
num= int(input("Enter a number: "))
for i in range(1,11,2):
    print(f"{num}x{i}={num*i}")
          