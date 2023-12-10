def get_gcd(x, y):
    while y:
        tmp = y
        if x % y == 0:
            return y
        y = x % y
        x = tmp

    return y


print(get_gcd(15, 21))
