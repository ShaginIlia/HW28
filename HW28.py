numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def odd(x):
    return x % 2


def mult_2(x):
    return x ** 2


result = map(mult_2, filter(odd, numbers))
print(list(result))
