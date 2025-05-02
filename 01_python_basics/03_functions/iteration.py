def factorial_iteration(n):
    result = 1
    for i in range(2,n+1):
        print(f"Before :  result: {result} and I is {i}")
        result *= i
        print(f"After : result: {result} and I is {i}")
        # result = result * i
    return result

factorial_iteration(5)