

def factorial_simple(n):
    for i in range(1, n):
        n = n * i
    return n
    
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial_simple(5))