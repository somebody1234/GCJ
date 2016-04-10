def f(N):
    seen = set()
    k = N

    while True:
        seen |= set(str(k))
        
        if len(seen) == 10:
            return k

        k += N

        if k > 10**7:
            print(N, k)

# 0 -> INSOMNIA

with open("A-small-attempt0.in") as infile:
    with open("a-small.out", "w") as outfile:    
        for case, line in enumerate(infile):
            if case == 0:
                continue

            n = int(line)

            print("Case #{}: {}".format(case, "INSOMNIA" if n == 0 else f(n)), file=outfile)
