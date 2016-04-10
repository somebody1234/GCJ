def small_div(n):
    for d in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if n%d == 0:
            return d
    return 0

j = 500
i = 2**31+1

print 'Case #1:'

while j:
    divs = []
    div = small_div(i)
    if div:
        divs += [div]
        s = bin(i)[2:]
        for base in range(3, 11):
            div = small_div(int(s, base))
            if div:
                divs += [div]
            else:
                break
        if len(divs) == 9:
            print s, ' '.join(map(str, divs))
            j -= 1
    i += 2