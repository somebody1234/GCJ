##import math
import sympy

def jamcoin():

##    with open("C-small-attempt0.in") as file:
##        lines = file.readlines()

    cases = []

    n = 16
    j = 50

##    n = 32
##    j = 500

    for num in range(2**(n-1)+1, 2**n, 2):
        a = bin(num)[2:]
        test = [a]

        for base in range(2, 11):
            z = int(a, base)
            m = 0
            if sympy.isprime(z):
                break
            else:
                m = sympy.factorint(z)
                test.append(str(sorted(list(m.keys()))[1]))

        if m:
            cases.append(" ".join(test)+"\n")
            print(cases[-1])
        if len(cases) == j:
            break

    cases = ["Case #1: \n"] + cases

    with open("C-small-attempt0.out", "w") as file:
        for string in cases:
            file.write(string)

jamcoin()
