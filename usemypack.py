#import mypack.myfunctions
from mypack.myfunctions import sum,table
from mypack.greets import sayhello
from mypack.coupons import getcouponcode
#r=sum(10,20)
# t=table(5)
# for i in t:
#     print(i)

# sayhello("John")

#sctrach=iter(getcouponcode())

#print(next(sctrach))

tables=map(table,[1,2,3,4,5,6,7,8,9,10])
for t in tables:
    for i in t:
        print(i)
