from itertools import product

N = 16
J = 50

print("Case #1:")

for i in product("01", repeat=N):
    if i[0] == "0" or i[-1] == "0":
        continue

    s = "".join(i)
    Y = []
    for j in range(2, 11):
        n = int(s, j)
        for k in range(2, int(n ** .5)):
            if n % k == 0:
                Y.append(k)
                break
        else:
            break
    else:
        print(s + " " + " ".join(map(str, Y)))
        J -= 1

        if not J:
            break
