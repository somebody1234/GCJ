#!/usr/bin/env python3

from itertools import product
import functools

@functools.lru_cache()
def is_composite(n):
    if n in [2, 3]: return False
    if n % 2 == 0: return 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            return i
        i += 2
    return False
    

with open('C-small-attempt0.in') as f:
    T, *cases = f.read().splitlines()
    
#N = 32
#J = 500

for i in range(int(T)):
    N, J = map(int, cases[i].split())
    num = 0
    for x in product('01', repeat=N-2):
        test = '1{}1'.format(''.join(x))
        facs = []
        good = True
        for base in range(2, 11):
            n = int(test, base)
            fac = is_composite(n)
            if fac:
                facs.append(fac)
            else:
                good = False
                break
        if good:
            num += 1
            print("{} {}".format(test, ' '.join(map(str, facs))))
        if num >= J:
            break
        