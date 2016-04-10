##from collections import deque
##
##def f(s):
##    L = deque()
##    L.append((s, 0))
##    S = set()
##
##    while L:
##        x, y = L.popleft()
##
##        if x in S:
##            continue
##
##        if all(c=="+" for c in x):
##            return y
##
##        S.add(x)
##
##        for i in range(len(x)):
##            new_x = "".join("+" if c=="-" else "-" for c in x[:i+1][::-1])+x[i+1:]
##            L.append((new_x, y+1))

import itertools
g=lambda s:len(list(itertools.groupby(s)))-1+(s[-1]=="-")

with open("B-small-attempt0.in") as infile:
    with open("B-small.out", "w") as outfile:
        next(infile)

        for case, s in enumerate(infile, start=1):
            s = s.rstrip()
            print("Case #{}: {}".format(case, g(s)), file=outfile)
