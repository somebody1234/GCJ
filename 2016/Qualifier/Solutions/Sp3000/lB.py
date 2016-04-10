import itertools
g=lambda s:len(list(itertools.groupby(s)))-1+(s[-1]=="-")

with open("B-large.in") as infile:
    with open("B-large.out", "w") as outfile:
        next(infile)

        for case, s in enumerate(infile, start=1):
            s = s.rstrip()
            print("Case #{}: {}".format(case, g(s)), file=outfile)
