def f(N):
    seen = set()
    k = N

    while True:
        seen |= set(str(k))
        
        if len(seen) == 10:
            return k

        k += N

# 0 -> INSOMNIA

with open("A-large.in") as infile:
    with open("A-large.out", "w") as outfile:
        next(infile)
        
        for case, line in enumerate(infile, start=1):
            n = int(line)
            print("Case #{}: {}".format(case, "INSOMNIA" if n == 0 else f(n)), file=outfile)
