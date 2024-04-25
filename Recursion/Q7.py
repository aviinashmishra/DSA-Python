# 7. Write a recursive function to calculate sum of first N natural numbers.



def SumN(n):
    if n==1:
        return 1
    return n + SumN(n-1)
print("Sum is", SumN(15))