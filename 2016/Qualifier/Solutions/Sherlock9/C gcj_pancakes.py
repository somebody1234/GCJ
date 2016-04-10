def pancakes():

    with open("B-small-attempt0.in") as file:
        lines = file.readlines()

    cases = []

    for index, test in enumerate(lines[1:]):

        test = test.strip()

        result = flips(test)

        cases.append("Case #{}: {}\n".format(index+1, result))

    with open("B-small-attempt0.out", 'w') as file:
        for string in cases:
            file.write(string)

def flips(test, total = 0):
    if test:
        last = test[-1]
        test = test[:-1]
        if last == "-":
            test = test.translate({43:45,45:43})
            total = total + 1
        return flips(test, total)
    else:
        return total

pancakes()
