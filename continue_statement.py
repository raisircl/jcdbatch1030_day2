# continue transfer the control to next round of the loop
# statement which followed by continue will not be executed for that time
#print all numbes 1 to 10 skip 5, 7
for i in range(1,11):
    if i==5 or i==7:
        continue
    print(i)    