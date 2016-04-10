import itertools

def fractile(n, c):
    L = [''.join(x) for x in itertools.product("G.", repeat=n)]

    for x in L:
        y = x
        for i in range(c-1):
            y = ''.join(x if c == '.' else 'G'*n for c in y)

        yield y

    # Take output lines and try qN/zee{[~\5b]}%$:p

def from_base(nums, b):
    total = 0

    for n in nums:
        total = total*b + n

    return total

with open("D-small-attempt0.in") as infile:
    with open("D-small.out", "w") as outfile:
        next(infile)

        for case, line in enumerate(infile, start=1):
            K, C, S = map(int, line.split())

            L = list(range(K))
            result = []

            for i in range(0, K, C):
                result.append(from_base(L[i:i+C], K) + 1)

            print("Case #{}: {}".format(case, "IMPOSSIBLE" if len(result) > S else " ".join(map(str, result))),
                    file=outfile)

            
