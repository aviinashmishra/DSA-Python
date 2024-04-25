# 3. Write a recursive function to print first N odd natural numbers.

def PrintNodd(n):
    if n>0:
        PrintNodd(n-1)
        print(2*n-1,end=" ")
PrintNodd(10)
