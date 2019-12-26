# -------------------------------------------------------


myadd = lambda x, y: x + y
print(myadd(2,3))


# -------------------------------------------------------


def myfn(n):
    a = map(lambda i: i ** i, range(1, n + 1))
    return sum(a)
print(myfn(3))