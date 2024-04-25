# 10. Write a recursive function to calculate factorial of a number.


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
print("Sum is", fact(15))