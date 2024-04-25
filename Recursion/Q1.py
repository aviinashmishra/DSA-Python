# 1. Write a recursive function to print first N natural numbers.


def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
printN(20)
