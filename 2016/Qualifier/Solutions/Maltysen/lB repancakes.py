import sys
import re

with open(sys.argv[1]) as f:
    cases = f.readlines()[1:]

    for i, case in enumerate(cases):
        n=0
        last = ""
        for k in case[:-1]:
            if k != last:
                n += 1
            last = k
        print("Case #{}: {}". format(i+1, n - 1 + (case[-2]=="-")))
