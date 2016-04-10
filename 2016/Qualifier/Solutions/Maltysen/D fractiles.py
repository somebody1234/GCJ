import sys

with open(sys.argv[1]) as f:
    cases = f.readlines()[1:]

    for i, case in enumerate(cases):
        K, C, S = map(int, case[:-1].split())

        print("Case #{0}: {1}".format(i + 1, " ".join(str(K**(C-1) * i + 1) for i in range(S))))
