# 4. Write a recursive function to print first N even natural numbers


def PrintNEven(n):
    if n>0:
        PrintNEven(n-1)
        print(2*n,end=" ")
PrintNEven(10)
