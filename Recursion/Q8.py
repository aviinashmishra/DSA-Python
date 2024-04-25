# 8. Write a recursive function to calculate sum of first N odd natural numbers


def SumNodd(n):
    if n==1:
        return 1
    return 2*n-1 + SumNodd(n-1)
print("Sum is", SumNodd(15))