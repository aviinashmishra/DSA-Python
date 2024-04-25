# 6. Write a recursive function to print first N even natural numbers in reverse order.



def RevrsePrintNEven(n):
    if n>0:
        print(2*n,end=" ")
        RevrsePrintNEven(n-1)
RevrsePrintNEven(10)