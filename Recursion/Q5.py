# 5. Write a recursive function to print first N odd natural numbers in reverse order.



def RevrsePrintNodd(n):
    if n>0:
        print(2*n-1,end=" ")
        RevrsePrintNodd(n-1)
RevrsePrintNodd(10)