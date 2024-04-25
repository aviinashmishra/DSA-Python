# 9. Write a recursive function to calculate sum of first N even natural numbers



def SumNEven(n):
    if n==2:
        return 2
    return 2*n + SumNEven(n-1)
print("Sum is", SumNEven(15))