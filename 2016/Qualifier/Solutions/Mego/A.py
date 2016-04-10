#!/usr/bin/env python3

with open("A-small-attempt0.in") as f:
    N, *cases = f.read().splitlines()
    
i = 0
    
for case in map(int, cases):
    i += 1
    if case == 0:
        print("Case #{}: INSOMNIA".format(i))
    else:
        seen = set()
        n = 1
        while len(seen) != 10:
            seen |= set(str(n*case))
            n += 1
        print("Case #{}: {}".format(i, (n-1)*case))