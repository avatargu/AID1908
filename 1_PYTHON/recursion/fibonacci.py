def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def list_fibonacci(n):
    list_fibo = []
    for item in range(n + 1):
        list_fibo.append(fibonacci(item))
    return list_fibo

print(fibonacci(10))
print(list_fibonacci(10))



