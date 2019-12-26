def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def sum_prime(m,n):
    result = 0
    for item in range(m,n + 1):
        if is_prime(item):
            result = result + item
    return result

if __name__ == "__main__":
    print(sum_prime(1,10))
