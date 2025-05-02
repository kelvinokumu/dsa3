def factorial(n):
    if n==0 or n==1:
        return 1
    print(n)
    return factorial(n - 1)

result = factorial(5)
print(result)