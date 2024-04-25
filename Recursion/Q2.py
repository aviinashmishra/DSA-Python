# 2. Write a recursive function to print first N natural numbers in reverse order.


def RevPrintN(n):
    if n>0:
        print(n,end=" ")
        RevPrintN(n-1)
RevPrintN(20)
