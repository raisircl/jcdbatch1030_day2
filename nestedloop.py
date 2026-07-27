'''
  1 2 3
1 * 
2 * *
3 * * *

'''
i=1
while i<=3:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1

# Dry Run
# i   j   condition   Condition output
# 1   1   i<=3 True   j<=2 True   *
# 1   2   i<=3 True   j<=2 True   * 
# 1   3   i<=3 True   j<=2 False  (new line)
# 2   1   i<=3 True   j<=2 True   *
# 2   2   i<=3 True   j<=2 True   * 
# 2   3   i<=3 True   j<=2 False  (new line)
# 3   1   i<=3 True   j<=2 True   *
# 3   2   i<=3 True   j<=2 True   *
# 3   3   i<=3 True   j<=2 False  (new line)
# 4   1   i<=3 False  (exit loop)
