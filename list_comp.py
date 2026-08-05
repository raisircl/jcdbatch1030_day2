pricelist=[3442,525,221,343,532,121,442,442,2554]
hpl=[price/2 if price>=1000 else price for price in pricelist]
print(hpl)

eolist=[f"{x} is even" if x%2==0 else f"{x} is odd" for x in pricelist]
for i in eolist:
    print(i)
    