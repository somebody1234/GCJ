def lowest_divisor(n):
    d = 3
    limit = int(n**0.5)
    while d <= limit + 1:
        if n%d == 0:
            return d
        d += 1
    return 0

j = 50
i = 2**15+1

print 'Case #1:'

while j:
    divs = []
    div = lowest_divisor(i)
    if div:
        divs += [div]
        s = bin(i)[2:]
        for base in range(3, 11):
            div = lowest_divisor(int(s, base))
            if div:
                divs += [div]
            else:
                break
        if len(divs) == 9:
            print s, ' '.join(map(str, divs))
            j -= 1
    i += 2