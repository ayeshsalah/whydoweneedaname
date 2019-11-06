## Example 1: Using looping technique
def fib(n):
    a,b = 1,1
    for _ in range(n-1):
        a,b = b,a+b
    return a


## Example 2: Using recursion
def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)

print(fib(5))
print(fibR(5))


