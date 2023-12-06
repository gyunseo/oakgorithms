import sys

sys.setrecursionlimit(10**9)


def get_karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    ac = get_karatsuba(a, c)
    bd = get_karatsuba(b, d)
    ad_bc = get_karatsuba(a + b, c + d) - ac - bd

    result = ac * 10 ** (2 * n2) + ad_bc * 10**n2 + bd

    return result


if __name__ == "__main__":
    x = 2462
    y = 8014
    print(get_karatsuba(x, y))
