import sympy


def get_primes_python(start, stop):
    dct = {x: True for x in list(range(start, stop + 1))}
    x = start

    while x ** 2 <= stop:
        if dct[x]:
            y = x ** 2
            while y <= stop:
                dct[y] = False
                y += x
        x += 1

    lst = []
    for x, y in dct.items():
        if y:
            lst.append(x)

    return lst


def get_primes_sympy(start, stop):
    return print(list(sympy.sieve.primerange(start, stop)))


get_primes_sympy(2, 10000000)
