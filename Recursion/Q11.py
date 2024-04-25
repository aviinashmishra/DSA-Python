# 11. Write a recursive function to calculate sum of squares of first N natural numbers


def SumNsquare(n):
    if n==1:
        return 1
    return n*n + SumNsquare(n-1)
print("Sum is", SumNsquare(5))