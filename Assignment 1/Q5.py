# 5. Write a Python script to create a list of first N terms of a Fibonacci 
N = int(input("Give me value of N: "))
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

print(f"The first {N} terms of the Fibonacci sequence are: {fibonacci(N)}")
