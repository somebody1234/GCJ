all_digits = set("0123456789")

with open(input()) as f, open("results.txt", "w") as out:
    cases = f.readlines()[1:]
    for i, N in enumerate(cases):
        digits = set()
        n = 1
        N = int(N)

        if not N:
            print("Case #{0}: INSOMNIA".format(i + 1), file=out)
            continue

        while digits != all_digits:
            digits |= set(str(n * N))

            n += 1

        print("Case #{0}: {1}".format(i + 1, str(n * N - N)), file=out)
